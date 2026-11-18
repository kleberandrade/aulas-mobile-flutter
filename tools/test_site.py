"""Behavioral checks for the published static course and its deep links."""
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'site' / 'dist'
SLUGS = [p.parent.name for p in sorted((ROOT / 'lessons').glob('*/README.md'))]


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.language = None
        self.exercises = 0
        self.headings = []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'html':
            self.language = attrs.get('lang')
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('script', 'img', 'link'):
            target = attrs.get('src') or attrs.get('href')
            if target:
                self.links.append(target)
        if attrs.get('class') == 'exercise':
            self.exercises += 1


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, 'tools/build_site.py'], cwd=ROOT, check=True)

    def test_every_module_has_five_exercises_in_both_languages(self):
        for language, prefix in [('pt-BR', ''), ('en', 'en/')]:
            for slug in SLUGS:
                with self.subTest(language=language, module=slug):
                    path = OUTPUT / prefix / 'modules' / slug / 'index.html'
                    doc = Document(path.read_text())
                    self.assertEqual(doc.language, language)
                    self.assertEqual(doc.exercises, 5)
                    self.assertIn('exercises', doc.ids)

    def test_all_local_links_and_assets_work_from_nested_pages(self):
        for path in OUTPUT.rglob('*.html'):
            doc = Document(path.read_text())
            for href in doc.links:
                link = urlsplit(href)
                if link.scheme or link.netloc:
                    continue
                target = (path.parent / unquote(link.path)).resolve() if link.path else path
                if target.is_dir():
                    target /= 'index.html'
                with self.subTest(page=path.relative_to(OUTPUT), link=href):
                    self.assertTrue(target.is_relative_to(OUTPUT))
                    self.assertTrue(target.is_file(), target)
                    if link.fragment and target.suffix == '.html':
                        self.assertIn(unquote(link.fragment), Document(target.read_text()).ids)

    def test_language_switch_retains_the_corresponding_module(self):
        for slug in SLUGS:
            for prefix in ['', 'en/']:
                path = OUTPUT / prefix / 'modules' / slug / 'index.html'
                text = path.read_text()
                self.assertIn('data-language-link', text)
                self.assertRegex(text, r'href="[^"]*modules/' + re.escape(slug) + r'/"')

    def test_translated_content_and_all_project_destinations_are_present(self):
        import json
        snapshot = json.loads((ROOT / 'docs/repository-snapshot.json').read_text())
        for prefix in ['', 'en/']:
            text = (OUTPUT / prefix / 'projects/index.html').read_text()
            for repo in snapshot['repositories']:
                self.assertIn(repo['url'], text)
        english = (OUTPUT / 'en/modules/01-dart/index.html').read_text()
        self.assertIn('Learning objectives', english)
        self.assertIn('Completion criteria', english)
        self.assertNotIn('Conclusão:', english)
        self.assertNotIn('Pré-requisitos', english)

    def test_books_and_masmorra_are_linked_and_site_has_no_remote_runtime_dependencies(self):
        for prefix in ['', 'en/']:
            text = (OUTPUT / prefix / 'books/index.html').read_text()
            self.assertIn('https://masmorra.io/', text)
            self.assertIn('https://kleberandrade.dev/', text)
        for path in OUTPUT.rglob('*.html'):
            text = path.read_text()
            self.assertNotRegex(text, r'<script[^>]+src="https?://')
            self.assertNotIn('cdn.tailwindcss.com', text)
            self.assertIn('class="skip-link"', text)

    def test_lesson_rendering_preserves_commands_and_escapes_raw_html(self):
        from build_site import markdown
        source = '## Reference\n\n<script>bad()</script>\n\n```sh\nflutter --version\ndart --version\n```\n\n- [Books](../../docs/books.md)\n'
        result = markdown(source, 'en/modules/01-dart/', 'en')
        self.assertIn('<h2>Reference</h2>', result)
        self.assertNotIn('<script>', result)
        self.assertIn('&lt;script&gt;', result)
        self.assertIn('flutter --version\ndart --version', result)
        self.assertIn('href="../../books/"', result)


if __name__ == '__main__':
    unittest.main()

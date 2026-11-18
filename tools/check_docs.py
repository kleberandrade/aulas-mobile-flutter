"""Check the course structure and local Markdown navigation without dependencies."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    '01-dart', '02-forms', '03-layouts', '04-apis', '05-local-data',
    '06-services', '07-firebase', '08-iot', '09-architecture', '10-final-project',
]


def anchors(text):
    counts = {}
    result = set()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f'{slug}-{count}')
    return result


def check():
    errors = []
    documents = list(ROOT.rglob('*.md'))
    for path in documents:
        text = path.read_text()
        visible = re.sub(r'^```.*?^```\s*$', '', text, flags=re.M | re.S)
        for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', visible):
            link = urlsplit(target)
            if link.scheme or link.netloc:
                continue
            resolved = (path.parent / unquote(link.path)).resolve() if link.path else path
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing local target {target}')
            elif link.fragment and resolved.suffix == '.md':
                if unquote(link.fragment) not in anchors(resolved.read_text()):
                    errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')

    actual = sorted(p.parent.name for p in (ROOT / 'lessons').glob('*/README.md'))
    if actual != MODULES:
        errors.append('Expected exactly the ten ordered course modules.')
    for module in MODULES:
        path = ROOT / 'lessons' / module / 'README.md'
        if not path.exists():
            continue
        text = path.read_text()
        for heading in ['Pré-requisitos', 'Objetivos', 'Atividade orientadora',
                        'Leitura sugerida', 'Estudos de caso e referências', 'Exercícios práticos']:
            if f'## {heading}\n' not in text:
                errors.append(f'{module}: missing {heading}')
        exercises = text.split('## Exercícios práticos\n')[-1]
        if re.findall(r'^(\d+)\. ', exercises, re.M) != ['1', '2', '3', '4', '5']:
            errors.append(f'{module}: expected exercises 1 through 5')
        if '## ' in exercises:
            errors.append(f'{module}: exercises must be the final section')
        for line in re.findall(r'^\d+\. .+', exercises, re.M):
            if 'Objetivo:' not in line or 'Conclusão:' not in line:
                errors.append(f'{module}: exercise needs objective and completion criteria')
        for entrypoint in ['README.md', 'README.pt-BR.md']:
            if f'(lessons/{module}/README.md)' not in (ROOT / entrypoint).read_text():
                errors.append(f'{entrypoint}: module {module} is not linked')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Checked {len(documents)} Markdown files, 10 modules and 50 exercises.')
    return 0


if __name__ == '__main__':
    sys.exit(check())

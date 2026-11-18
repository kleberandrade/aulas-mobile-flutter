"""Build the bilingual course as dependency-free, deep-linkable static pages."""
from pathlib import Path
import html
import hashlib
import json
import os
import re
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site/dist'
REPO = 'https://github.com/kleberandrade/aulas-mobile-flutter'
PUBLIC = 'https://kleberandrade.github.io/aulas-mobile-flutter/'
TEXT = {
    'pt': dict(lang='pt-BR', course='Desenvolvimento Mobile', hub='ACERVO DE AULAS', modules='Módulos', exercises='Exercícios', books='Livros e sites', projects='Projetos', guide='Guia de estudo', resources='Referências', skip='Pular para o conteúdo', language='Idioma', menu='Abrir navegação', close='Fechar navegação', learn='Objetivos de aprendizagem', prerequisites='Pré-requisitos', activity='Atividade orientadora', reading='Leitura sugerida', references='Estudos de caso e referências', objective='Objetivo', criteria='Critério de conclusão', next='Próximo módulo', previous='Módulo anterior', view='Explorar módulo', practice='Praticar', source='Ver aula no GitHub', search='Buscar assunto ou módulo', empty='Nenhum módulo encontrado. Tente outro termo.', found='módulos encontrados', code='Repositório atual', article='Artigo relacionado', archive='Acervo histórico', author='Prof. Kleber de Oliveira Andrade · Fatec Americana', intro='Um percurso de Dart e Flutter, da lógica aos aplicativos completos. Aulas, exercícios e leituras para aprender construindo.', title='Da primeira linha a um app completo.', start='Começar a estudar', all='Ver os projetos', path='O SEU PERCURSO', foundations='Fundamentos', foundations_note='Dart, formulários e interfaces', data='Dados e integrações', data_note='APIs, persistência, serviços e IoT', delivery='Arquitetura e entrega', delivery_note='Organização, testes e trabalho final', path_title='Um assunto de cada vez.', path_note='Siga a sequência ou encontre o tema que precisa revisar.', exercise_title='Aprender é colocar em prática.', exercise_note='Cada módulo termina com cinco desafios, objetivos claros e critérios para conferir a sua entrega.', projects_title='Estudos de caso, código de verdade.', projects_intro='Os repositórios atuais são o ponto de partida para executar os aplicativos. Consulte seus READMEs para versões, plataformas e configuração.', projects_note='Os links acompanham os projetos modernizados. Artigos históricos podem usar versões anteriores; compare-os com a implementação atual.', snapshot='Consultar o registro dos repositórios', footer='Material de aula, código de referência e leituras para a próxima etapa.', licensed='Material do repositório sob licença MIT. Obras externas mantêm seus próprios direitos.', back='Voltar aos módulos', catalog='Catálogo completo do autor', documents='Documentação', no_app='Os aplicativos ficam em seus próprios repositórios. Este site organiza o caminho de estudo.', steps='10 módulos', challenges='50 exercícios', cases='23 repositórios', current='CÓDIGO ATUALIZADO', read='Abrir referência', learn_more='Continue a explorar', selected='Idioma selecionado', modules_label='Navegação pelos módulos'),
    'en': dict(lang='en', course='Mobile Development', hub='COURSE LIBRARY', modules='Modules', exercises='Exercises', books='Books & sites', projects='Projects', guide='Study guide', resources='Resources', skip='Skip to content', language='Language', menu='Open navigation', close='Close navigation', learn='Learning objectives', prerequisites='Prerequisites', activity='Suggested activity', reading='Suggested reading', references='Case studies and references', objective='Objective', criteria='Completion criteria', next='Next module', previous='Previous module', view='Explore module', practice='Practice', source='View lesson on GitHub', search='Search a topic or module', empty='No modules found. Try a different topic.', found='modules found', code='Current repository', article='Related article', archive='Historical archive', author='Prof. Kleber de Oliveira Andrade · Fatec Americana', intro='A Dart and Flutter learning path, from programming foundations to complete applications. Lessons, exercises and readings for learning by building.', title='From your first line to a complete app.', start='Start learning', all='Explore the projects', path='YOUR LEARNING PATH', foundations='Foundations', foundations_note='Dart, forms and interfaces', data='Data & integrations', data_note='APIs, persistence, services and IoT', delivery='Architecture & delivery', delivery_note='Organization, tests and final assignment', path_title='One topic at a time.', path_note='Follow the sequence or find the topic you want to revisit.', exercise_title='Make learning tangible.', exercise_note='Every module ends with five challenges, clear objectives and observable criteria for reviewing your work.', projects_title='Case studies. Real source code.', projects_intro='The current repositories are the starting point for running the applications. Read their READMEs for versions, supported platforms and configuration.', projects_note='These links point to the modernized projects. Historical articles may use older versions; compare them with the current implementation.', snapshot='View the repository snapshot', footer='Course material, reference code and readings for your next step.', licensed='Repository material is MIT licensed. External works retain their own rights.', back='Back to modules', catalog="Author’s complete catalog", documents='Documentation', no_app='Applications live in their own repositories. This site brings the learning path together.', steps='10 modules', challenges='50 exercises', cases='23 repositories', current='CURRENT SOURCE CODE', read='Open reference', learn_more='Keep exploring', selected='Selected language', modules_label='Module navigation')
}
TEXT['pt'].update(labs='Laboratórios', labs_title='Explore, entenda e leve para o seu app.', labs_intro='Sete laboratórios interativos e sete pacotes Dart para experimentar conceitos e transformar o aprendizado em código.', open_lab='Abrir laboratório', package='Pacote no pub.dev', source_code='Código-fonte', lab_modules='Use nestes módulos', lab_practice='Laboratórios para este módulo', lab_explore='Explorar no navegador', lab_integrate='Aplicar no projeto da aula', lab_outcome='O que conferir', lab_context='As atividades relacionam o laboratório ao tema da aula. As propostas de integração são adaptações para o seu projeto.', sections='Neste módulo', lab_heading='Experimente antes de integrar.', lab_home_note='Explore no navegador, consulte os exemplos e use os pacotes Dart nos seus próprios projetos.', lab_home_cta='Conhecer os laboratórios', lab_count='7 laboratórios · 7 pacotes Dart', package_version='Versão consultada no pub.dev')
TEXT['en'].update(labs='Labs & packages', labs_title='Explore, understand, build it into your app.', labs_intro='Seven interactive laboratories and seven Dart packages for experimenting with concepts and turning learning into code.', open_lab='Open laboratory', package='Package on pub.dev', source_code='Source code', lab_modules='Use in these modules', lab_practice='Labs for this module', lab_explore='Explore in the browser', lab_integrate='Apply in your course project', lab_outcome='What to check', lab_context='These activities connect each laboratory to the lesson. Integration suggestions are adaptations for your own project.', sections='In this module', lab_heading='Experiment before you integrate.', lab_home_note='Explore in the browser, read the examples and use the Dart packages in your own projects.', lab_home_cta='Explore the laboratories', lab_count='7 laboratories · 7 Dart packages', package_version='Version checked on pub.dev')
TEXT['pt'].update(footer_rights='Obras externas mantêm seus próprios direitos.',footer_learn='Aprender',footer_explore='Explorar',footer_about='Sobre o curso',footer_repo='Repositório',footer_history='Histórico das aulas',footer_books='Livros do autor',footer_license='Licença MIT',change_language='Alterar idioma',current_language='Atual')
TEXT['en'].update(footer_rights='External works retain their own rights.',footer_learn='Learn',footer_explore='Explore',footer_about='About the course',footer_repo='Repository',footer_history='Course history',footer_books="Author’s books",footer_license='MIT license',change_language='Change language',current_language='Current')
TEXT['pt'].update(books_title='Leituras para acompanhar sua jornada.',books_intro='Capas oficiais e sugestões para aprofundar os temas de cada módulo.',book_cover='Capa de',book_catalog='Explorar o catálogo completo',reading_resources='Continue a leitura',showcase_title='Veja o que você vai construir.',showcase_intro='Capturas reais dos estudos de caso do curso. Explore a interface e depois acompanhe o código no repositório.',view_case='Ver estudo de caso')
TEXT['en'].update(books_title='Readings for your learning journey.',books_intro='Official covers and suggestions for exploring each module in more depth.',book_cover='Cover of',book_catalog='Explore the full catalog',reading_resources='Keep reading',showcase_title='See what you can build.',showcase_intro='Actual screenshots from the course case studies. Explore the interface, then follow the source in its repository.',view_case='View case study')
SLUGS = [p.parent.name for p in sorted((ROOT / 'lessons').glob('*/README.md'))]
EN = {}
SNAPSHOT = {}
LABS = {}
BOOKS = {}


def esc(value):
    return html.escape(str(value), quote=True)


def route(locale, key='home'):
    prefix = 'en/' if locale == 'en' else ''
    return prefix if key == 'home' else prefix + key.strip('/') + '/'


def link_from(current, target):
    base = OUT / current
    return os.path.relpath(OUT / target, base).replace(os.sep, '/') + ('/' if target.endswith('/') or not target else '')


def asset(current,name):
    digest=hashlib.sha256((ROOT/'site/assets'/name).read_bytes()).hexdigest()[:12]
    return link_from(current,'assets/'+name)+'?v='+digest


def href(current, locale, key='home', anchor=''):
    return link_from(current, route(locale, key)) + ('#' + anchor if anchor else '')


def resource_link(url, current, locale):
    if urlsplit(url).scheme or url.startswith('#'):
        return url
    mappings = {'books.md':'books', 'resources.md':'resources', 'study-guide.md':'guide', 'case-studies.md':'projects'}
    for name, key in mappings.items():
        if url.endswith(name):
            return href(current, locale, key)
    if url.endswith(('README.md', 'README.pt-BR.md')) and 'history' not in url:
        return href(current, locale)
    return REPO + '/blob/master/' + url.lstrip('./')


def inline(text, current, locale):
    text = esc(text)
    text = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', lambda m: '<a href="' + esc(resource_link(html.unescape(m[2]), current, locale)) + '">' + m[1] + '</a>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)


class MarkdownWriter:
    def __init__(self,current,locale):
        self.current=current
        self.locale=locale
        self.blocks=[]
        self.paragraph=[]
        self.listing=None
        self.code=None

    def flush(self):
        if self.paragraph:
            self.blocks.append('<p>'+inline(' '.join(self.paragraph),self.current,self.locale)+'</p>')
            self.paragraph.clear()

    def end_list(self):
        if self.listing:
            self.blocks.append('</'+self.listing+'>')
            self.listing=None

    def fence(self):
        self.flush()
        self.end_list()
        if self.code is None:
            self.code=[]
        else:
            self.blocks.append('<pre><code>'+esc('\n'.join(self.code))+'</code></pre>')
            self.code=None

    def heading(self,line):
        self.flush()
        self.end_list()
        match=re.match(r'^(#{1,6})\s+(.*)',line)
        if match:
            level=max(2,min(len(match[1]),4))
            self.blocks.append(f'<h{level}>'+inline(match[2],self.current,self.locale)+f'</h{level}>')

    def list_item(self,line):
        self.flush()
        kind='ul' if line.startswith(('-','*')) else 'ol'
        if self.listing!=kind:
            self.end_list()
            self.blocks.append('<'+kind+'>')
            self.listing=kind
        item=re.sub(r'^([-*]|\d+\.)\s+','',line)
        self.blocks.append('<li>'+inline(item,self.current,self.locale)+'</li>')

    def line(self,line):
        if line.startswith('```'):
            self.fence()
        elif self.code is not None:
            self.code.append(line)
        elif line.startswith('#'):
            self.heading(line)
        elif re.match(r'^[-*] |^\d+\. ',line):
            self.list_item(line)
        elif line.strip():
            self.end_list()
            self.paragraph.append(line.strip())
        else:
            self.flush()
            self.end_list()


def markdown(text,current,locale):
    writer=MarkdownWriter(current,locale)
    for line in text.splitlines()+['']:
        writer.line(line)
    return '\n'.join(writer.blocks)


def pt_module(slug):
    text = (ROOT / 'lessons' / slug / 'README.md').read_text()
    sections = dict(re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', text, re.M | re.S))
    activity = sections['Atividade orientadora'].strip().split('\n\n')
    exercises = []
    for title, objective, criteria in re.findall(r'^\d+\. \*\*(.*?)\.\*\* Objetivo: (.*?) Conclusão: (.*)$', sections['Exercícios práticos'], re.M):
        exercises.append(dict(title=title, objective=objective, criteria=criteria))
    return dict(title=text.splitlines()[0].split(' · ',1)[1], prerequisites=sections['Pré-requisitos'].strip(), objectives=sections['Objetivos'].strip(), activity=activity[0], note='\n\n'.join(activity[1:]), reading=sections['Leitura sugerida'].strip(), exercises=exercises)


def module(locale, slug):
    return EN['modules'][slug] if locale == 'en' else pt_module(slug)


def module_refs(slug):
    text = (ROOT / 'lessons' / slug / 'README.md').read_text()
    return list(dict.fromkeys(re.findall(r'https://github.com/kleberandrade/[\w-]+', text)))


def language_links(current,key,locale):
    t=TEXT[locale]
    active_flag='br' if locale=='pt' else 'uk'
    active_name='Português brasileiro' if locale=='pt' else 'English'
    options=[]
    for lang,label,flag in [('pt','Português brasileiro','br'),('en','English','uk')]:
        selected=' aria-current="true"' if lang==locale else ''
        status=f'<small>{t["current_language"]}</small>' if lang==locale else ''
        options.append(f'<a class="language-option" data-language-link="{lang}" href="{href(current,lang,key)}" hreflang="{TEXT[lang]["lang"]}" lang="{TEXT[lang]["lang"]}" aria-label="{label}"{selected}><img src="{asset(current,flag+".svg")}" alt="" width="24" height="24"><span>{label}</span>{status}</a>')
    return f'<div class="languages"><details class="language-picker"><summary class="language-trigger" role="button" aria-label="{t["language"]}: {active_name}" title="{t["change_language"]}"><img src="{asset(current,active_flag+".svg")}" alt="" width="25" height="25"></summary><div class="language-menu" role="group" aria-label="{t["language"]}">{"".join(options)}</div></details></div>'


def footer(locale,current):
    t=TEXT[locale]
    groups=[
        (t['footer_learn'],[(t['modules'],href(current,locale,'home','modules')),(t['exercises'],href(current,locale,'home','practice')),(t['guide'],href(current,locale,'guide'))]),
        (t['footer_explore'],[(t['labs'],href(current,locale,'labs')),(t['books'],href(current,locale,'books')),(t['projects'],href(current,locale,'projects')),(t['resources'],href(current,locale,'resources'))]),
        (t['footer_about'],[(t['footer_repo'],REPO),(t['footer_history'],REPO+'/blob/master/docs/history/README-2019-2020.md'),(t['footer_books'],'https://kleberandrade.dev/#books')])
    ]
    navigation=''.join('<section class="footer-group"><h2>'+title+'</h2>'+''.join('<a href="'+url+'">'+label+'</a>' for label,url in links)+'</section>' for title,links in groups)
    return f'<footer class="site-footer"><div class="footer-intro"><a class="brand" href="{href(current,locale)}"><img src="{asset(current,"logo.svg")}" alt="" width="38" height="38"><span>{t["course"]}<small>DART & FLUTTER</small></span></a><p>{t["footer"]}</p><a class="footer-author" href="https://kleberandrade.dev/">Kleber de Oliveira Andrade</a></div><div class="footer-links">{navigation}</div><div class="footer-bottom"><span>{t["author"]}</span><span><a href="{REPO}/blob/master/LICENSE">{t["footer_license"]}</a> · {t["footer_rights"]}</span></div></footer>'


def shell(locale, key, title, body, description=None):
    t = TEXT[locale]; current = route(locale, key)
    logo = asset(current,'logo.svg')
    navigation = ''.join(f'<a href="{href(current,locale,k,a)}"' + (' aria-current="page"' if key == k and k != 'home' else '') + f'>{t[label]}</a>' for label,k,a in [('modules','home','modules'),('labs','labs',''),('books','books',''),('projects','projects',''),('guide','guide','')])
    fulltitle = title + ' · Dart & Flutter'
    document = f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(description or t['intro'])}"><meta name="theme-color" content="#02569b"><title>{esc(fulltitle)}</title><link rel="canonical" href="{PUBLIC+current}"><link rel="alternate" hreflang="pt-BR" href="{PUBLIC+route('pt',key)}"><link rel="alternate" hreflang="en" href="{PUBLIC+route('en',key)}"><link rel="icon" href="{logo}" type="image/svg+xml"><link rel="stylesheet" href="{asset(current,'site.css')}"><script src="{asset(current,'site.js')}" defer></script></head>
<body data-locale="{locale}" data-page="{key}" data-found="{t['found']}"><a class="skip-link" href="#main">{t['skip']}</a>
<header class="site-header"><div class="header-inner"><a class="brand" aria-label="{t['course']} · Dart and Flutter" href="{href(current,locale)}"><img src="{logo}" alt="" width="40" height="40"><span>{t['course']}<small>DART & FLUTTER</small></span></a><button class="menu-toggle" aria-label="{t['menu']}" data-open-label="{t['menu']}" data-close-label="{t['close']}" aria-expanded="false" aria-controls="primary-nav"><span></span><span></span></button><nav id="primary-nav" aria-label="{t['modules_label']}">{navigation}<a class="nav-github" href="{REPO}">GitHub </a></nav>{language_links(current,key,locale)}</div></header>
<noscript><style>.menu-toggle{{display:none}}.header-inner{{flex-wrap:wrap}}.header-inner>nav{{display:flex;position:static;flex-wrap:wrap;order:3;width:100%}}</style></noscript><main id="main">{body}</main>{footer(locale,current)}</body></html>'''
    path = OUT / current / 'index.html'; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(document)


def module_lab_terms(slug,locale):
    identifiers={item['lab'] for item in LABS['modules'][slug]}
    return ' '.join(lab['title']+' '+lab['package']+' '+' '.join(lab['topics'][locale]) for lab in LABS['labs'] if lab['id'] in identifiers)


def module_cards(locale, practice=False):
    t=TEXT[locale]; current=route(locale)
    cards=[]
    for i, slug in enumerate(SLUGS,1):
        m=module(locale,slug); anchor='exercises' if practice else ''
        if practice:
            cards.append(f'<a class="practice-link" href="{href(current,locale,"modules/"+slug,anchor)}"><span>{i:02}</span>{esc(m["title"])}</a>')
        else:
            cards.append(f'<a class="module-card" data-module data-search="{esc(m["title"]+" "+m["objectives"]+" "+module_lab_terms(slug,locale))}" href="{href(current,locale,"modules/"+slug)}"><div class="card-top"><span class="module-number">{i:02}</span><span class="pill">5 {t["exercises"].lower()}</span></div><h3>{esc(m["title"])}</h3><p>{esc(m["objectives"])}</p><span class="card-link">{t["view"]}</span></a>')
    return ''.join(cards)


def home(locale):
    t=TEXT[locale]; current=route(locale)
    stages=''.join(f'<div class="path-stage"><span>0{i}</span><div><h3>{t[title]}</h3><p>{t[note]}</p></div></div>' for i,title,note in [(1,'foundations','foundations_note'),(2,'data','data_note'),(3,'delivery','delivery_note')])
    body=f'''<section class="hero wrap"><div class="hero-copy"><p class="eyebrow"><span></span>{t['hub']} · FATEC AMERICANA</p><h1>{t['title']}</h1><p class="hero-description">{t['intro']}</p><div class="actions"><a class="button" href="{href(current,locale,'modules/'+SLUGS[0])}">{t['start']} </a><a class="text-link" href="{href(current,locale,'labs')}">{t['lab_home_cta']}</a></div><div class="hero-stats"><span><b>10</b>{t['modules']}</span><span><b>50</b>{t['exercises']}</span><span><b>7</b>{t['labs']}</span><span><b>23</b>{t['projects']}</span></div></div><div class="path-note"><div class="note-top"><h2>{t['path']}</h2></div>{stages}<div class="note-bottom"><span>Dart · Flutter · Apps</span><span aria-hidden="true">✦</span></div></div></section>
<section class="wrap lab-callout"><div><span class="lab-tag">{t['lab_count']}</span><h2>{t['lab_heading']}</h2><p>{t['lab_home_note']}</p></div><a class="button" href="{href(current,locale,'labs')}">{t['lab_home_cta']}</a></section>
<section id="modules" class="section wrap"><div class="section-heading"><div><p class="eyebrow">01 / {t['modules'].upper()}</p><h2>{t['path_title']}</h2><p>{t['path_note']}</p></div><div class="search-box"><label for="module-search">{t['search']}</label><input id="module-search" type="search" autocomplete="off" placeholder="Dart, API, neural…"><p id="search-status" role="status" aria-live="polite"></p></div></div><div class="module-grid">{module_cards(locale)}</div><p id="search-empty" hidden>{t['empty']}</p></section>
{course_showcase(locale,current)}
<section id="practice" class="practice-section"><div class="wrap practice-layout"><div><p class="eyebrow">02 / {t['exercises'].upper()}</p><h2>{t['exercise_title']}</h2><p>{t['exercise_note']}</p><a class="text-link" href="{href(current,locale,'guide')}">{t['guide']} </a></div><div class="practice-list">{module_cards(locale,True)}</div></div></section>
<section class="wrap explore-section"><p class="eyebrow">03 / {t['learn_more'].upper()}</p><div class="explore-grid"><a href="{href(current,locale,'books')}"><span aria-hidden="true">✦</span><h2>{t['books']}</h2><p>Masmorra ASCII · O Grimório dos Padrões · Fantasia Técnica</p></a><a href="{href(current,locale,'projects')}"><span aria-hidden="true">&lt;/&gt;</span><h2>{t['projects']}</h2><p>{t['no_app']}</p></a></div></section>'''
    shell(locale,'home',t['course'],body)


def module_page(locale,slug,index):
    t=TEXT[locale]; current=route(locale,'modules/'+slug); m=module(locale,slug)
    sidebar=''.join(f'<a href="{href(current,locale,"modules/"+s)}"'+(' aria-current="page"' if s==slug else '')+f'><span>{i:02}</span>{esc(module(locale,s)["title"])}</a>' for i,s in enumerate(SLUGS,1))
    refs=''.join(f'<li><a href="{url}">{esc(url.rsplit("/",1)[-1])} </a></li>' for url in module_refs(slug))
    exercises=''.join(f'<li class="exercise" id="exercise-{i}"><span class="exercise-number">{i:02}</span><div><h3>{esc(e["title"])}</h3><p><strong>{t["objective"]}:</strong> {inline(e["objective"],current,locale)}</p><p class="criteria"><strong>{t["criteria"]}:</strong> {inline(e["criteria"],current,locale)}</p></div></li>' for i,e in enumerate(m['exercises'],1))
    steps=[]
    for label,j in [('previous',index-1),('next',index+1)]:
        if 0<=j<len(SLUGS):steps.append(f'<a href="{href(current,locale,"modules/"+SLUGS[j])}"><small>{t[label]}</small><strong>{esc(module(locale,SLUGS[j])["title"])}</strong></a>')
    body=f'''<div class="wrap lesson-layout"><aside class="lesson-sidebar"><a class="back-link" href="{href(current,locale,'home','modules')}"> {t['back']}</a><p class="eyebrow">{t['modules']}</p><nav aria-label="{t['modules_label']}">{sidebar}</nav></aside><article class="lesson-article"><p class="eyebrow">{t['modules'].upper()} / {index+1:02} · DART & FLUTTER</p><h1>{esc(m['title'])}</h1><div class="lesson-shortcuts"><a class="button" href="#exercises">{t['practice']} · 5 </a><a class="text-link" href="{REPO}/blob/master/lessons/{slug}/README.md">{t['source']} </a></div><nav class="module-tabs" aria-label="{t['sections']}"><a href="#objectives">{t['learn']}</a><a href="#labs">{t['labs']}</a><a href="#exercises">{t['exercises']}</a></nav><section class="prerequisites"><h2>{t['prerequisites']}</h2>{markdown(m['prerequisites'],current,locale)}</section><section id="objectives"><h2>{t['learn']}</h2>{markdown(m['objectives'],current,locale)}</section><section><h2>{t['activity']}</h2>{markdown(m['activity'],current,locale)}<div class="note">{markdown(m['note'],current,locale)}</div></section><section><h2>{t['reading']}</h2>{markdown(m['reading'],current,locale)}<a href="{href(current,locale,'books')}">{t['books']} </a></section><section><h2>{t['references']}</h2><ul>{refs}<li><a href="{href(current,locale,'resources')}">{t['resources']}</a></li></ul></section>{lab_suggestions(locale,slug,current)}<section id="exercises" class="exercise-section"><p class="eyebrow">05 / {t['exercises'].upper()}</p><h2>{t['exercises']}</h2><ol class="exercise-list">{exercises}</ol></section><nav class="lesson-next" aria-label="{t['modules_label']}">{''.join(steps)}</nav></article></div>'''
    shell(locale,'modules/'+slug,m['title'],body,m['objectives'])


def translated_document(locale,key):
    content=EN[key]; chunks=[]
    for section in content['sections']:
        chunks.append('## '+section['title'])
        chunks.extend(section.get('paragraphs',[]))
        chunks.extend('- '+s for s in section.get('bullets',[]))
        chunks.extend('- ['+x['title']+']('+x['url']+')'+(': '+x['description'] if x.get('description') else '') for x in section.get('links',[]))
    return content['title'],content['intro'],'\n\n'.join(chunks)


def document_page(locale,key,filename):
    t=TEXT[locale]; current=route(locale,key)
    if locale=='en': title,intro,content=translated_document(locale,key)
    else:
        text=(ROOT/'docs'/filename).read_text();title=text.splitlines()[0].lstrip('# '); intro=''; content='\n'.join(text.splitlines()[4:])
    # The original Markdown starts with an index-navigation line already handled by the site shell.
    body=f'<div class="wrap document-layout"><div class="document-heading"><p class="eyebrow">DART & FLUTTER / {t[key].upper()}</p><h1>{esc(title)}</h1><p>{esc(intro)}</p></div><article class="prose">{markdown(content,current,locale)}</article></div>'
    shell(locale,key,title,body)


PROJECT_NOTES={
    'calculadora-imc-aulas-flutter':('Formulários e cálculo de IMC.','Forms and BMI calculation.'), 'interest-calculator-flutter':('Formulários e cálculo de juros.','Forms and interest calculations.'), 'floor-calculator-flutter':('Estimativa de pisos e revestimentos.','Flooring and tile estimates.'), 'marcador-truco-aulas-flutter':('Placar e interação em um jogo de cartas.','Scoring and interaction for a card game.'), 'calculadora-flutter':('Operações e interface de calculadora.','Calculator operations and interface.'), 'tic-tac-toe-flutter':('Jogo da velha e regras de estado.','Tic-tac-toe and game state.'), 'search-cep-aulas-flutter':('Consulta de endereços por CEP.','Brazilian postal-code address lookup.'), 'quiz-covid19-flutter':('Questionário, dados e respostas.','Quiz questions, data and answers.'), 'movies-flutter':('Catálogo e consulta de filmes.','Movie browsing and queries.'), 'todo-list-aulas-flutter':('Lista de tarefas e persistência.','Task lists and persistence.'), 'borrowed-stuff-flutter':('Registro de objetos emprestados.','Tracking borrowed items.'), 'my-money-fluter':('Finanças pessoais e armazenamento.','Personal finances and storage.'), 'chatbot-aulas-flutter':('Interface de conversa e serviços.','Conversation interface and services.'), 'teachable-ml-flutter':('Classificação de imagens.','Image classification.'), 'lost-and-found-flutter':('Achados, perdidos e devoluções.','Lost items, found items and returns.'), 'trampo-flutter':('Agenda e gestão de pequenos serviços.','Scheduling and small-service management.'), 'adotai-flutter':('Catálogo e fluxo de adoção de animais.','Pet listings and adoption workflows.'), 'mqtt_aulas_flutter':('Mensagens e integrações MQTT.','MQTT messages and integrations.'), 'controlled-robot-arduino':('Controle de robô e Bluetooth.','Robot control and Bluetooth.'), 'my-blood-flutter':('Campanhas comunitárias de doação.','Community blood-donation campaigns.'), 'soap-factory-flutter':('Ingredientes, fórmulas e lotes.','Ingredients, formulas and batches.'), 'roguelike-dart':('Jogo de terminal para praticar Dart.','A terminal game for practicing Dart.'), 'o-grimorio-dos-padroes':('Padrões de projeto com exemplos em TypeScript.','Design patterns with TypeScript examples.')}


def projects(locale):
    t=TEXT[locale];cards=[]
    for repo in SNAPSHOT['repositories']:
        name=repo['name'];note=PROJECT_NOTES[name][0 if locale=='pt' else 1]
        articles=''.join(f'<a href="{esc(url)}">{t["article"]} </a>' for url in repo.get('article_links_from_current_readme',[]))
        cards.append(f'<article class="project-card"><span class="eyebrow">{t["current"]}</span><h2>{esc(name)}</h2><p>{note}</p><div class="project-links"><a href="{repo["url"]}">{t["code"]} </a>{articles}</div></article>')
    body=f'<section class="wrap document-heading"><p class="eyebrow">DART & FLUTTER / 23 {t["projects"].upper()}</p><h1>{t["projects_title"]}</h1><p>{t["projects_intro"]}</p><div class="note">{t["projects_note"]} <a href="{REPO}/blob/master/docs/repository-snapshot.json">{t["snapshot"]} </a></div></section><section class="wrap project-grid">{"".join(cards)}</section>'
    shell(locale,'projects',t['projects'],body)


def course_showcase(locale,current):
    t=TEXT[locale]
    cases=[
        ('floor','floor-calculator-flutter',('Formulários e medidas','Forms and measurements'),('Entradas e unidades no planejador de pisos e revestimentos.','Inputs and units in the flooring and tile planner.')),
        ('calculator','calculadora-flutter',('Layouts e operações','Layouts and operations'),('Estado da interface, operações e feedback na calculadora.','Interface state, operations and feedback in the calculator.')),
        ('tic-tac-toe','tic-tac-toe-flutter',('Interação e regras de jogo','Interaction and game rules'),('Turnos e feedback visual em uma partida de jogo da velha.','Turns and visual feedback in a tic-tac-toe match.'))
    ]
    cards=[]
    index=0 if locale=='pt' else 1
    for image_name,repo,titles,descriptions in cases:
        title=titles[index]
        cards.append(f'<figure class="showcase-item"><a href="https://github.com/kleberandrade/{repo}"><img src="{asset(current,"showcase/"+image_name+".jpg")}" alt="{esc(title)}" width="390" height="844" loading="lazy" decoding="async"></a><figcaption><strong>{title}</strong><p>{descriptions[index]}</p><a href="https://github.com/kleberandrade/{repo}">{t["view_case"]}</a></figcaption></figure>')
    return f'<section class="wrap course-showcase"><h2>{t["showcase_title"]}</h2><p>{t["showcase_intro"]}</p><div class="showcase-grid">{"".join(cards)}</div></section>'


def books_page(locale):
    t=TEXT[locale];current=route(locale,'books');cards=[]
    for book in BOOKS['books']:
        links=''.join(f'<a href="{href(current,locale,"modules/"+slug)}">{esc(module(locale,slug)["title"])}</a>' for slug in book['modules'])
        cards.append(f'<article class="book-card"><a class="book-cover" href="{book["url"]}"><img src="{asset(current,book["image"])}" alt="{t["book_cover"]} {esc(book["title"])}" width="{book["width"]}" height="{book["height"]}" loading="lazy" decoding="async"></a><div class="book-info"><h3><a href="{book["url"]}">{esc(book["title"])}</a></h3><p>{esc(book["description"][locale])}</p><div class="book-module-links">{links}</div></div></article>')
    resources=[('Masmorra ASCII','https://masmorra.io/'),('Masmorra · '+('Sumário' if locale=='pt' else 'Contents'),'https://masmorra.io/livro'),('Masmorra · '+('Código por capítulo' if locale=='pt' else 'Code by chapter'),'https://masmorra.io/codigo'),('O Grimório dos Padrões','https://o-grimorio-dos-padroes.vercel.app/'),('Fantasia Técnica','https://fantasia-tecnica.vercel.app/'),('Fantasia Ágil','https://fantasia-agil.vercel.app/')]
    more=''.join('<li><a href="'+url+'">'+label+'</a></li>' for label,url in resources)
    body=f'<section class="wrap document-heading"><p class="eyebrow">DART & FLUTTER / {t["books"].upper()}</p><h1>{t["books_title"]}</h1><p>{t["books_intro"]}</p></section><section class="wrap book-collection"><h2 class="sr-only">{t["books"]}</h2><div class="book-grid">{"".join(cards)}</div><p class="image-attribution">{esc(BOOKS["attribution"][locale])}</p></section><section class="wrap document-layout"><div class="prose"><h2>{t["reading_resources"]}</h2><ul>{more}</ul><p><a href="https://kleberandrade.dev/#books">{t["book_catalog"]}</a></p></div></section>'
    shell(locale,'books',t['books'],body)


def lab_actions(lab,locale,primary=False):
    t=TEXT[locale]
    style=' class="button"' if primary else ''
    return f'<div class="lab-actions"><a{style} href="{lab["lab_url"]}">{t["open_lab"]}</a><a href="{lab["package_url"]}">{t["package"]}</a><a href="{lab["repo"]}">{t["source_code"]}</a></div>'


def lab_suggestions(locale,slug,current):
    t=TEXT[locale]
    registry={lab['id']:lab for lab in LABS['labs']}
    cards=[]
    for suggestion in LABS['modules'][slug]:
        lab=registry[suggestion['lab']]
        kind=t['lab_explore'] if suggestion['kind']=='explore' else t['lab_integrate']
        cards.append(f'<article class="lab-suggestion"><span class="lab-tag">{kind}</span><h3><a href="{lab["lab_url"]}">{esc(lab["title"])}</a></h3><p>{esc(suggestion["activity"][locale])}</p><p class="criteria"><strong>{t["lab_outcome"]}:</strong> {esc(suggestion["outcome"][locale])}</p>{lab_actions(lab,locale)}</article>')
    return f'<section id="labs" class="lab-suggestions"><h2>{t["lab_practice"]}</h2><p>{t["lab_context"]}</p>{"".join(cards)}<a href="{href(current,locale,"labs")}">{t["lab_home_cta"]}</a></section>'


def laboratories(locale):
    t=TEXT[locale];current=route(locale,'labs');cards=[]
    for lab in LABS['labs']:
        topics=''.join('<span>'+esc(topic)+'</span>' for topic in lab['topics'][locale])
        connections=[]
        for slug in SLUGS:
            if any(item['lab']==lab['id'] for item in LABS['modules'][slug]):
                connections.append(f'<a href="{href(current,locale,"modules/"+slug,"labs")}">{esc(module(locale,slug)["title"])}</a>')
        cards.append(f'<article class="lab-card" id="{lab["id"]}"><span class="lab-tag">DART + FLUTTER</span><h2>{esc(lab["title"])}</h2><p>{esc(lab["description"][locale])}</p><div class="lab-topics">{topics}</div><div class="package-status"><code>{esc(lab["package"])}</code><span title="{t["package_version"]}">v{esc(lab["version"])}</span></div>{lab_actions(lab,locale,True)}<div class="lab-module-links"><small>{t["lab_modules"]}</small>{"".join(connections)}</div></article>')
    body=f'<section class="wrap document-heading lab-intro"><p class="eyebrow">{t["lab_count"]}</p><h1>{t["labs_title"]}</h1><p>{t["labs_intro"]}</p></section><section class="wrap lab-grid">{"".join(cards)}</section>'
    shell(locale,'labs',t['labs'],body)


def validate_labs():
    identifiers={lab['id'] for lab in LABS['labs']}
    if len(identifiers)!=7 or len(LABS['labs'])!=7:
        raise ValueError('Expected the seven course laboratories')
    if set(LABS['modules'])!=set(SLUGS):
        raise ValueError('Laboratory suggestions must cover every module')
    for suggestions in LABS['modules'].values():
        if not suggestions:
            raise ValueError('A module has no laboratory suggestions')
        for item in suggestions:
            if item['lab'] not in identifiers or item['kind'] not in ['explore','integrate']:
                raise ValueError('Unknown laboratory or activity kind')


def main():
    global EN,SNAPSHOT,LABS,BOOKS
    EN=json.loads((ROOT/'site/content/en.json').read_text())
    SNAPSHOT=json.loads((ROOT/'docs/repository-snapshot.json').read_text())
    LABS=json.loads((ROOT/'site/content/labs.json').read_text())
    BOOKS=json.loads((ROOT/'site/content/books.json').read_text())
    validate_labs()
    if set(EN['modules'])!=set(SLUGS):raise ValueError('English module coverage is incomplete')
    for slug in SLUGS:
        if len(EN['modules'][slug]['exercises'])!=5 or len(pt_module(slug)['exercises'])!=5:raise ValueError('Expected five exercises per module: '+slug)
    if OUT.exists():shutil.rmtree(OUT)
    OUT.mkdir(parents=True);shutil.copytree(ROOT/'site/assets',OUT/'assets')
    for locale in ['pt','en']:
        home(locale)
        for i,slug in enumerate(SLUGS):module_page(locale,slug,i)
        for key,filename in [('guide','study-guide.md'),('resources','resources.md')]:document_page(locale,key,filename)
        books_page(locale)
        projects(locale)
        laboratories(locale)
    (OUT/'.nojekyll').write_text('')
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+PUBLIC+'sitemap.xml\n')
    urls=[PUBLIC+str(p.relative_to(OUT)).replace('index.html','') for p in sorted(OUT.rglob('index.html'))]
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(url)+'</loc></url>' for url in urls)+'</urlset>')
    print(f'Built {len(urls)} static pages in {OUT}')


if __name__=='__main__':main()

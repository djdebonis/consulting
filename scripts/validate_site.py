"""Validate a Hugo build without third-party dependencies.
Usage: python3 scripts/validate_site.py /path/to/build
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET

root = Path(sys.argv[1]).resolve()
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.tags=[]; self.ids=[]; self.links=[]; self.schemas=[]; self.in_schema=False; self.schema=''
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a: self.ids.append(a['id'])
        for key in ('href','src'):
            if a.get(key): self.links.append(a[key])
        if tag=='script' and a.get('type')=='application/ld+json': self.in_schema=True; self.schema=''
    def handle_data(self, data):
        if self.in_schema:self.schema+=data
    def handle_endtag(self, tag):
        if tag=='script' and self.in_schema:
            self.schemas.append(json.loads(self.schema));self.in_schema=False

pages={p:Page(p) for p in root.rglob('*.html')}
errors=[]; count=0
for path,page in pages.items():
    # Hugo pagination aliases are redirect documents, not content pages.
    if any(t=='meta' and a.get('http-equiv','').lower()=='refresh' for t,a in page.tags):continue
    count+=1
    def check(condition, message):
        if not condition:errors.append(f'{path.relative_to(root)}: {message}')
    check(sum(t=='h1' for t,a in page.tags)==1,'expected one H1')
    check(sum(t=='main' for t,a in page.tags)==1,'expected main landmark')
    check(any(t=='html' and a.get('lang') for t,a in page.tags),'missing language')
    check(len(page.ids)==len(set(page.ids)),'duplicate IDs')
    for key,tag,attr in [('description','meta','name'),('canonical','link','rel'),('og:title','meta','property'),('og:image','meta','property'),('og:url','meta','property')]:
        check(sum(t==tag and a.get(attr)==key for t,a in page.tags)==1,f'expected one {key}')
    check(len(page.schemas)==1,'expected one JSON-LD graph')
    for t,a in page.tags:
        if t=='img': check('alt' in a,'image missing alt')
        if t=='button': check(bool(a.get('aria-label')),'unlabeled button')
    for schema in page.schemas:
        for entity in schema['@graph']:
            if entity['@type']=='ProfilePage':check(path.relative_to(root).as_posix() in ['index.html','about-david-debonis/index.html'],'incorrect ProfilePage')
    for link in page.links:
        url=urlsplit(link)
        if url.scheme and url.scheme not in ['http','https']:continue
        if url.netloc and url.netloc!='davidjdebonis.info':continue
        target=(root/unquote(url.path).lstrip('/')) if url.path.startswith('/') else (path.parent/unquote(url.path))
        if not url.path:target=path
        if target.is_dir():target=target/'index.html'
        check(target.exists(),f'missing resource {link}')
        if target in pages and url.fragment:check(unquote(url.fragment) in pages[target].ids,f'missing anchor {link}')
for path in root.rglob('*.xml'):ET.parse(path)
index=json.loads((root/'index.json').read_text())
assert any(p['permalink']=='/work/' for p in index)
assert not any('Markdown Syntax' in p['title'] for p in index)
assert 'https://davidjdebonis.info/sitemap.xml' in (root/'robots.txt').read_text()
sitemap=(root/'sitemap.xml').read_text()
assert '/tags/' not in sitemap and '/categories/' not in sitemap
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {count} HTML pages; internal links and anchors, resources, metadata, JSON-LD, landmarks, image alt text, unique IDs, XML, search index, sitemap, robots.')

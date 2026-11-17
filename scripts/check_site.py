from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote

root=Path(__file__).resolve().parents[1]/'_site'
assert (root/'index.html').is_file()
errors=[]
class Links(HTMLParser):
    def __init__(self,page):super().__init__();self.page=page
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for key in ['href','src']:
            value=a.get(key,'');u=urlsplit(value)
            if not value or u.scheme or u.netloc or not u.path:continue
            target=(root/unquote(u.path).lstrip('/')) if u.path.startswith('/') else self.page.parent/unquote(u.path)
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(f'{self.page.relative_to(root)} → {value}')
for page in root.rglob('*.html'):Links(page).feed(page.read_text())
assert not errors,'Missing local links:\n'+'\n'.join(errors)
for path in ['projects/index.html','writing/index.html','about.html','studies/fifa-hidden-gems/index.html','studies/agora-match/index.html','studies/football-forecasting/index.html','demos/scouting.html']:
    assert (root/path).is_file(),path
print('PASS: required pages and local links/assets.')

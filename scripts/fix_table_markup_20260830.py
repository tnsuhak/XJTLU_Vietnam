from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
bad = '<th scope="col"ead>'
count = s.count(bad)
if count:
    s = s.replace(bad, '<thead>')
    p.write_text(s, encoding='utf-8')
    print(f'Fixed {count} malformed <thead> tag(s).')
else:
    print('No malformed <thead> tags found.')

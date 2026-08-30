from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
changed = False

# Repair a malformed <thead> pattern left by an older accessibility edit.
bad = '<th scope="col"ead>'
count = s.count(bad)
if count:
    s = s.replace(bad, '<thead>')
    changed = True
    print(f'Fixed {count} malformed <thead> tag(s).')
else:
    print('No malformed <thead> tags found.')

# Give the first cell of each body row row-header semantics. This improves
# table relationships for screen readers and machine parsing while retaining
# the same visual treatment via the dedicated CSS below.
def convert_tbody(match):
    body = match.group(1)
    updated = re.sub(
        r'(<tr(?:\s[^>]*)?>)\s*<td([^>]*)>(.*?)</td>',
        lambda m: f'{m.group(1)}<th scope="row"{m.group(2)}>{m.group(3)}</th>',
        body,
        flags=re.S,
    )
    return f'<tbody>{updated}</tbody>'

new_s = re.sub(r'<tbody>(.*?)</tbody>', convert_tbody, s, flags=re.S)
if new_s != s:
    s = new_s
    changed = True
    print('Added semantic row headers to table bodies.')
else:
    print('Table body row headers already semantic.')

css_marker = '/* TNS_SEMANTIC_ROW_HEADERS */'
css_anchor = 'td .vnd{display:block;font-size:12px;color:var(--muted)}\n'
css = '''/* TNS_SEMANTIC_ROW_HEADERS */
tbody th[scope="row"]{background:transparent;color:var(--ink-2);text-align:left;padding:14px 16px;border-top:1px solid var(--line);vertical-align:top;font-weight:400;font-size:14px;letter-spacing:0;border-radius:0}
tbody th[scope="row"] b{color:var(--navy);font-weight:600}
tr:hover th[scope="row"],tr:hover td{background:#fbfaf6}
'''
if css_marker not in s:
    if css_anchor not in s:
        raise SystemExit('Table CSS anchor missing')
    s = s.replace(css_anchor, css_anchor + css, 1)
    changed = True
    print('Added row-header visual compatibility CSS.')

if changed:
    p.write_text(s, encoding='utf-8')
else:
    print('No table changes required.')

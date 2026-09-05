from pathlib import Path
import re
import subprocess

p = Path('index.html')
text = p.read_text(encoding='utf-8')

# If the old long layout is still present, run the one-time structural converter.
if '<!-- ===================== VIETNAM RELEVANCE ===================== -->' not in text or '<!-- ===================== STUDENT LIFE ===================== -->' not in text:
    subprocess.run(['python', 'scripts/lighten_homepage_student_life_20260905.py'], check=True)
    text = p.read_text(encoding='utf-8')
else:
    # The legacy helper may re-add contextual blocks after section IDs. Remove
    # those because the compact sections already contain their own detail links.
    text = re.sub(
        r'\n?<!-- TNS_INLINE_GUIDE_[A-Z_]+_START -->.*?<!-- TNS_INLINE_GUIDE_[A-Z_]+_END -->\n?',
        '\n',
        text,
        flags=re.S,
    )
    text = text.replace('href="#rooms">Ký túc xá', 'href="#rooms">Đời sống sinh viên')
    p.write_text(text, encoding='utf-8')
    print('Existing light homepage preserved; legacy inline guides removed')

# Stories/news compaction is safe to re-run on the current layout.
subprocess.run(['python', 'scripts/lighten_homepage_stories_20260905.py'], check=True)

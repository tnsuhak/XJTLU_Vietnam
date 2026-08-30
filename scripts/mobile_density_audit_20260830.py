from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# 1) Keep FAQ content crawlable but collapsed by default on initial load.
s = re.sub(r'<details class="qa"\s+open>', '<details class="qa">', s)

# 2) Shorten admission-panel introductions. Detailed criteria remain immediately
# below in the structured rows/cards, so the intro does not need to repeat them.
replacements = {
    '''<p class="sub">Năm 1 là năm nền tảng (Foundation Year) giúp bạn làm quen với phương pháp học tập của Anh Quốc, tiếng Anh học thuật và các môn cơ sở; từ năm 2 bắt đầu chuyên ngành theo chương trình 3 năm của Liverpool.</p>''':
    '''<p class="sub">Năm 1 là năm nền tảng; từ năm 2 bắt đầu học chuyên ngành.</p>''',

    '''<p class="sub">Dành cho sinh viên đã hoàn thành ít nhất năm 1 tại một trường đại học được công nhận. Bạn vào thẳng năm chuyên ngành đầu tiên của chương trình Liverpool.</p>''':
    '''<p class="sub">Dành cho sinh viên đã hoàn thành ít nhất 1 năm đại học; xét theo hồ sơ và độ phù hợp ngành.</p>''',

    '''<p class="sub">Dành cho sinh viên đã hoàn thành 2 năm trở lên cùng ngành hoặc ngành rất gần. Hạn nộp hồ sơ chuyển tiếp năm 3 thường sớm hơn (giữa tháng 5).</p>''':
    '''<p class="sub">Dành cho sinh viên đã hoàn thành ít nhất 2 năm cùng ngành hoặc ngành gần.</p>''',

    '''<p class="lead" style="margin-bottom:22px">Học sinh có bằng cấp quốc tế được <b>xét tuyển thẳng vào năm 2</b> (chương trình 3 năm). Nếu gần đạt, bạn vẫn có thể được nhận vào năm 1. Tiếng Anh cho năm 2: IELTS 6.5 (không kỹ năng nào dưới 5.5) hoặc TOEFL iBT 90; một số bằng có thể được miễn.</p>''':
    '''<p class="lead" style="margin-bottom:22px">Bằng quốc tế đạt yêu cầu có thể <b>vào thẳng năm 2</b>. Tiếng Anh: IELTS 6.5 (mỗi kỹ năng ≥ 5.5) hoặc TOEFL iBT 90; một số bằng có thể được miễn.</p>''',
}
for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new, 1)

# 3) Mobile-density pass: reduce oversized prose/spacing, keep desktop/tablet
# unchanged, make admissions tabs horizontally scrollable instead of four tall
# wrapped rows, and keep FAQ answers compact when opened.
marker = '/* TNS_MOBILE_DENSITY_AUDIT */'
if marker not in s:
    css = r'''
/* TNS_MOBILE_DENSITY_AUDIT */
@media(max-width:640px){
  body{font-size:15px;line-height:1.58}
  .section{padding:54px 0}
  .section-head{margin-bottom:26px}
  h2{font-size:28px;line-height:1.16;margin-bottom:12px}
  h3{font-size:20px}
  .lead{font-size:15px;line-height:1.58}
  .eyebrow{font-size:10.5px;letter-spacing:.14em;margin-bottom:10px}

  /* Admissions: one compact horizontal row of tabs on bar phones. */
  .adm-tabs{width:100%;max-width:100%;flex-wrap:nowrap;overflow-x:auto;overscroll-behavior-x:contain;scroll-snap-type:x proximity;scrollbar-width:none;border-radius:16px;margin-bottom:18px;padding:4px;gap:4px}
  .adm-tabs::-webkit-scrollbar{display:none}
  .adm-tab{flex:0 0 auto;scroll-snap-align:start;padding:10px 14px;font-size:13px;line-height:1.25;white-space:nowrap}
  #admission .adm-panel>.lead{font-size:14.5px;line-height:1.55;margin-bottom:16px!important}
  .req-main{padding:20px}
  .req-main h3{font-size:22px;line-height:1.22}
  .req-main .sub{font-size:13.5px;line-height:1.55;margin-bottom:14px}
  .req-row{padding:11px 0;font-size:13.5px;line-height:1.55}
  .req-side{gap:10px}
  .req-side .card{padding:18px}
  .req-side .card p,.req-side .card li{font-size:13.5px;line-height:1.55}
  .intl{gap:10px}
  .intl .card{padding:18px}
  .intl .v{font-size:26px}
  .intl p{font-size:13px;line-height:1.55}
  .timeline,.process{margin-top:38px}

  /* FAQ: all closed initially; compact typography when a user opens one. */
  .faq{gap:8px}
  .qa summary{padding:15px 16px;gap:10px;font-size:14px;line-height:1.45}
  .qa summary .q{font-size:18px;width:18px}
  .qa summary .chev{width:19px;height:19px}
  .qa .a{padding:0 16px 17px 44px;font-size:13.5px;line-height:1.58}

  /* Repeated cards/long-form sections: denser mobile reading rhythm. */
  .story{padding:20px;gap:10px}
  .story p{font-size:13.5px;line-height:1.58}
  .partner-card{padding:20px 18px}
  .partner-card p{font-size:13.5px;line-height:1.58}
  .faculty{padding:24px;gap:20px}
  .faculty h3{font-size:24px}
  .faculty p{font-size:14px;line-height:1.58}
  .cta-band{padding:48px 0}
  .inq-side{padding:26px 22px}
  .inq-side h3{font-size:26px}
  .inq-side p{font-size:14px;line-height:1.58}
  .contact-list li{font-size:13.5px}

  /* News styles are declared later in the body; stronger selectors keep the
     mobile cards compact without changing desktop presentation. */
  body .tns-news-body{padding:18px}
  body .tns-news-body h3{font-size:18px;line-height:1.35}
  body .tns-news-body p{font-size:13.5px;line-height:1.55}
}
'''
    anchor = '</style>\n<script type="application/ld+json">'
    if anchor not in s:
        raise SystemExit('Main stylesheet closing anchor not found')
    s = s.replace(anchor, css + '\n</style>\n<script type="application/ld+json">', 1)

p.write_text(s, encoding='utf-8')
print('Applied mobile density audit: compact type/spacing, horizontal admission tabs, FAQ closed by default.')

from pathlib import Path

MARK_START = '<!-- TNS_AEO_GEO_START -->'
MARK_END = '<!-- TNS_AEO_GEO_END -->'

blocks = {
    'du-hoc-trung-quoc-2027.html': '''
<!-- TNS_AEO_GEO_START -->
<section aria-labelledby="aeo-china-study" style="background:#f6f2e8;border:1px solid #eadfbf;border-radius:18px;padding:24px 26px;margin:0 0 30px">
  <div style="font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#1f6f78">Trả lời nhanh</div>
  <h2 id="aeo-china-study" style="margin:7px 0 10px;font-size:26px">Du học Trung Quốc có bắt buộc phải học bằng tiếng Trung không?</h2>
  <p style="margin:0"><strong>Không.</strong> Tùy trường và chương trình, sinh viên quốc tế có thể học bằng tiếng Trung hoặc tiếng Anh. XJTLU tại Tô Châu là một lựa chọn English-taught: trường cho biết các chương trình cấp bằng được giảng dạy bằng tiếng Anh, trong khi tiếng Trung có thể học thêm để hỗ trợ sinh hoạt và cơ hội nghề nghiệp.</p>
  <p style="margin:12px 0 0;font-size:13px;color:#667085">Cập nhật: 30/08/2026 · Nguồn chính: <a href="https://www.xjtlu.edu.cn/en/study/why-study-at-xjtlu" target="_blank" rel="noopener">XJTLU – Why Study at XJTLU?</a></p>
</section>
<!-- TNS_AEO_GEO_END -->''',
    'du-hoc-trung-quoc-bang-tieng-anh-xjtlu.html': '''
<!-- TNS_AEO_GEO_START -->
<section aria-labelledby="aeo-english-xjtlu" style="background:#f6f2e8;border:1px solid #eadfbf;border-radius:18px;padding:24px 26px;margin:0 0 30px">
  <div style="font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#1f6f78">Trả lời nhanh</div>
  <h2 id="aeo-english-xjtlu" style="margin:7px 0 10px;font-size:26px">Có thể học đại học bằng tiếng Anh tại Trung Quốc ở XJTLU không?</h2>
  <p style="margin:0"><strong>Có.</strong> Xi'an Jiaotong-Liverpool University (XJTLU) là đại học liên doanh quốc tế tại Tô Châu. XJTLU cho biết các chương trình cấp bằng được giảng dạy bằng tiếng Anh; sinh viên đại học đáp ứng yêu cầu tốt nghiệp nhận bằng XJTLU và bằng University of Liverpool.</p>
  <p style="margin:12px 0 0;font-size:13px;color:#667085">Cập nhật: 30/08/2026 · Nguồn chính: <a href="https://www.xjtlu.edu.cn/en/about" target="_blank" rel="noopener">XJTLU – About</a></p>
</section>
<!-- TNS_AEO_GEO_END -->''',
    'xjtlu-dieu-kien-tuyen-sinh-vietnam-2027.html': '''
<!-- TNS_AEO_GEO_START -->
<section aria-labelledby="aeo-vietnam-entry" style="background:#f6f2e8;border:1px solid #eadfbf;border-radius:18px;padding:24px 26px;margin:0 0 30px">
  <div style="font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#1f6f78">Trả lời nhanh</div>
  <h2 id="aeo-vietnam-entry" style="margin:7px 0 10px;font-size:26px">Học sinh Việt Nam cần gì để vào năm 1 XJTLU?</h2>
  <p style="margin:0">Theo yêu cầu quốc gia XJTLU đang công bố cho Việt Nam, Bằng Tốt Nghiệp Phổ Thông Trung Học được xem xét với điểm trung bình khoảng <strong>7/10</strong>, yêu cầu môn liên quan và kết quả kỳ thi tốt nghiệp THPT. Yêu cầu tiếng Anh năm 1 hiện là <strong>IELTS 5.0</strong> (mỗi kỹ năng từ 4.5) hoặc <strong>TOEFL iBT 62</strong>. Tiêu chí có thể thay đổi theo kỳ và ngành.</p>
  <p style="margin:12px 0 0;font-size:13px;color:#667085">Cập nhật: 30/08/2026 · Nguồn chính: <a href="https://www.xjtlu.edu.cn/en/admissions/global/qualifications" target="_blank" rel="noopener">XJTLU – Country/Region Entry Requirements</a> · <a href="https://www.xjtlu.edu.cn/en/admissions/ug/global/entry-requirements" target="_blank" rel="noopener">English Requirements</a></p>
</section>
<!-- TNS_AEO_GEO_END -->''',
    'xjtlu-hoc-phi-hoc-bong-2027.html': '''
<!-- TNS_AEO_GEO_START -->
<section aria-labelledby="aeo-xjtlu-scholarship" style="background:#f6f2e8;border:1px solid #eadfbf;border-radius:18px;padding:24px 26px;margin:0 0 30px">
  <div style="font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#1f6f78">Trả lời nhanh</div>
  <h2 id="aeo-xjtlu-scholarship" style="margin:7px 0 10px;font-size:26px">XJTLU có học bổng cho sinh viên quốc tế không?</h2>
  <p style="margin:0"><strong>Có.</strong> XJTLU công bố Entry Scholarship lên đến <strong>50% học phí mỗi năm</strong> cho ứng viên quốc tế bậc đại học có thành tích học tập xuất sắc. Học bổng có thể được gia hạn hằng năm nếu sinh viên tiếp tục duy trì kết quả học tập tốt theo quy định. Học phí, ưu đãi và thời hạn của từng kỳ cần được kiểm tra lại trước khi nộp hồ sơ.</p>
  <p style="margin:12px 0 0;font-size:13px;color:#667085">Cập nhật: 30/08/2026 · Nguồn chính: <a href="https://www.xjtlu.edu.cn/en/admissions/global/fees-and-scholarships/" target="_blank" rel="noopener">XJTLU – Fees and Scholarships</a></p>
</section>
<!-- TNS_AEO_GEO_END -->''',
    'xjtlu-ranking-2027.html': '''
<!-- TNS_AEO_GEO_START -->
<section aria-labelledby="aeo-xjtlu-ranking" style="background:#f6f2e8;border:1px solid #eadfbf;border-radius:18px;padding:24px 26px;margin:0 0 30px">
  <div style="font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#1f6f78">Trả lời nhanh</div>
  <h2 id="aeo-xjtlu-ranking" style="margin:7px 0 10px;font-size:26px">XJTLU có ranking riêng hay dùng ranking của University of Liverpool?</h2>
  <p style="margin:0"><strong>XJTLU có thứ hạng riêng.</strong> Xi'an Jiaotong-Liverpool University là một đại học độc lập được University of Liverpool và Xi'an Jiaotong University đồng sáng lập. Vì vậy khi đánh giá “XJTLU ranking”, cần dùng thứ hạng của chính XJTLU; thứ hạng của hai trường sáng lập là dữ liệu riêng.</p>
  <p style="margin:12px 0 0;font-size:13px;color:#667085">Cập nhật: 30/08/2026 · Nguồn chính: <a href="https://www.xjtlu.edu.cn/en/about" target="_blank" rel="noopener">XJTLU – About</a></p>
</section>
<!-- TNS_AEO_GEO_END -->'''
}

for filename, block in blocks.items():
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    if MARK_START in text:
        print(f'{filename}: AEO/GEO block already present; skipped')
        continue
    anchor = '<main class="main"><div class="wrap">'
    if anchor not in text:
        raise SystemExit(f'{filename}: main wrapper anchor missing')
    text = text.replace(anchor, anchor + block, 1)
    path.write_text(text, encoding='utf-8')
    print(f'{filename}: AEO/GEO direct-answer block added')

# Homepage: insert a compact entity-answer section immediately before the SEO guide cluster.
home = Path('index.html')
text = home.read_text(encoding='utf-8')
if MARK_START not in text:
    anchor = '<!-- TNS_SEO_GUIDES_START -->'
    if anchor not in text:
        raise SystemExit('index.html: SEO guide marker missing')
    block = '''
<!-- TNS_AEO_GEO_START -->
<section class="section" aria-labelledby="aeo-xjtlu-what" style="padding-top:54px;padding-bottom:18px">
  <div class="container">
    <div style="max-width:900px;background:#f6f2e8;border:1px solid #eadfbf;border-radius:20px;padding:28px 30px">
      <div style="font-size:12px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:#1f6f78">Trả lời nhanh · XJTLU Vietnam</div>
      <h2 id="aeo-xjtlu-what" style="margin:8px 0 12px">XJTLU là trường gì?</h2>
      <p style="margin:0"><strong>Xi'an Jiaotong-Liverpool University (XJTLU)</strong> là đại học liên doanh quốc tế tại Tô Châu, Trung Quốc, do Xi'an Jiaotong University và University of Liverpool đồng sáng lập. XJTLU cho biết các chương trình cấp bằng được giảng dạy bằng tiếng Anh; sinh viên đại học đáp ứng yêu cầu tốt nghiệp nhận bằng XJTLU và bằng University of Liverpool.</p>
      <p style="margin:14px 0 0;font-size:13px;color:#667085">Cập nhật: 30/08/2026 · Nguồn chính: <a href="https://www.xjtlu.edu.cn/en/about" target="_blank" rel="noopener">XJTLU – About</a></p>
    </div>
  </div>
</section>
<!-- TNS_AEO_GEO_END -->
'''
    text = text.replace(anchor, block + anchor, 1)
    home.write_text(text, encoding='utf-8')
    print('index.html: XJTLU entity direct-answer block added')
else:
    print('index.html: AEO/GEO block already present; skipped')

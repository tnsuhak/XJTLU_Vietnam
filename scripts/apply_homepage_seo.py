from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

replacements = {
    "XJTLU Việt Nam | Học bằng tiếng Anh tại Trung Quốc, nhận bằng Đại học Liverpool":
        "XJTLU Vietnam (Việt Nam) | Học phí, học bổng & tuyển sinh 2027",
    "XJTLU (Xi'an Jiaotong-Liverpool University) tại Tô Châu, Trung Quốc: học hoàn toàn bằng tiếng Anh và nhận bằng University of Liverpool (Anh Quốc). Ngành học, học phí, học bổng, điều kiện tuyển sinh và chi phí sinh hoạt dành cho học sinh Việt Nam.":
        "XJTLU Vietnam: thông tin tuyển sinh 2027 dành cho học sinh Việt Nam về học phí XJTLU, học bổng, điều kiện đầu vào, ngành học, ký túc xá và bằng University of Liverpool.",
    "Học hoàn toàn bằng tiếng Anh tại Tô Châu, nhận bằng University of Liverpool (Anh Quốc) và bằng XJTLU. Ngành học, học phí, học bổng và điều kiện tuyển sinh cho học sinh Việt Nam.":
        "XJTLU Vietnam 2027: học phí, học bổng, điều kiện tuyển sinh, ngành học và bằng University of Liverpool dành cho sinh viên Việt Nam.",
    "Học hoàn toàn bằng tiếng Anh tại Tô Châu, nhận bằng University of Liverpool (Anh Quốc) và bằng XJTLU.":
        "XJTLU Vietnam 2027: học phí, học bổng, tuyển sinh và bằng University of Liverpool.",
    "<span class=\"h1-brand\">XJTLU · Xi'an Jiaotong-Liverpool University</span>":
        "<span class=\"h1-brand\">XJTLU Vietnam · Xi'an Jiaotong-Liverpool University</span>",
    "Xi'an Jiaotong-Liverpool University (XJTLU) do <b>University of Liverpool</b> (Anh Quốc) và <b>Đại học Giao thông Tây An</b> (Trung Quốc) đồng sáng lập năm 2006. Sinh viên tốt nghiệp đại học nhận <b>bằng của University of Liverpool (Anh Quốc) và bằng của XJTLU</b>, học hoàn toàn bằng tiếng Anh, và có thể bổ sung tiếng Trung như một lợi thế nghề nghiệp.":
        "XJTLU Vietnam cung cấp thông tin dành cho học sinh và phụ huynh Việt Nam về <b>học phí XJTLU, học bổng, điều kiện tuyển sinh 2027, ngành học và ký túc xá</b>. Xi'an Jiaotong-Liverpool University (XJTLU) do <b>University of Liverpool</b> (Anh Quốc) và <b>Đại học Giao thông Tây An</b> (Trung Quốc) đồng sáng lập năm 2006. Sinh viên tốt nghiệp đại học nhận <b>bằng của University of Liverpool (Anh Quốc) và bằng của XJTLU</b>, học hoàn toàn bằng tiếng Anh, và có thể bổ sung tiếng Trung như một lợi thế nghề nghiệp."
}

changed = False
for old, new in replacements.items():
    if old in html:
        html = html.replace(old, new)
        changed = True

if not changed:
    print("No matching SEO strings found; homepage may already be patched.")
else:
    path.write_text(html, encoding="utf-8")
    print("Homepage SEO strings updated.")

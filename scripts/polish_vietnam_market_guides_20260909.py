from pathlib import Path

FAQ={
'xjtlu-to-chau-thuong-hai-viet-nam.html':[
('Tô Châu có gần Thượng Hải không?','Có. Tàu cao tốc từ Shanghai Hongqiao đến Tô Châu thường mất khoảng 25–30 phút; XJTLU SIP cách sân bay Hongqiao khoảng 70 km.'),
('Tô Châu có quan hệ kinh tế đáng kể với Việt Nam không?','Có. Năm 2025 thương mại Tô Châu – Việt Nam đạt khoảng 204,75 tỷ RMB; Việt Nam hiện là đối tác thương mại lớn thứ hai của Tô Châu và lớn nhất trong ASEAN.'),
('Học ở Tô Châu có nghĩa phải làm việc tại Trung Quốc sau tốt nghiệp không?','Không. Điểm mạnh là có thêm trải nghiệm Trung Quốc và hiểu thị trường trong khi học bằng tiếng Anh; kế hoạch nghề nghiệp có thể ở Việt Nam, Trung Quốc hoặc thị trường khác.')],
'xjtlu-chi-phi-sinh-hoat-2027.html':[
('Sinh viên XJTLU cần bao nhiêu tiền sinh hoạt mỗi tháng?','Ba mức tham khảo hiện tại là khoảng 3.700 RMB cho lối sống tiết kiệm, 6.450 RMB cho mức phổ biến và 9.600 RMB cho lối sống thoải mái hơn.'),
('Có nên đổi toàn bộ ngân sách sang VND ngay từ đầu không?','Không nên cố định tỷ giá quá sớm. Các khoản chính được tính bằng RMB, vì vậy nên giữ ngân sách gốc bằng RMB và quy đổi VND gần thời điểm thanh toán.'),
('Học phí đã bao gồm ký túc xá và sinh hoạt chưa?','Không. Học phí, chỗ ở, sinh hoạt, bảo hiểm, visa, đi lại và chi tiêu cá nhân cần được tính riêng.')],
'xjtlu-ky-tuc-xa-sip-taicang.html':[
('Sinh viên XJTLU ở SIP có ký túc xá trong campus không?','Các lựa chọn quốc tế chính nằm trong khu Dushu Lake gần campus và được đơn vị bên ngoài quản lý; XJTLU hỗ trợ sinh viên trong quá trình đặt chỗ.'),
('Sinh viên chương trình Taicang có ở Taicang ngay từ năm 1 không?','Không. Sinh viên đại học Year 1 của các chương trình XEC Taicang bắt đầu tại SIP và nên đặt chỗ ở SIP cho năm đầu.'),
('Taicang có phòng đơn không?','Có. XJTLU Entrepreneur Apartment có twin room và single room; giá năm học hiện được niêm yết lần lượt 6.000 RMB/giường và 14.000 RMB/phòng.')]
}

REPL={
'xjtlu-chi-phi-sinh-hoat-2027.html':{
'XJTLU đưa ra ba kịch bản tham khảo khoảng':'Ba kịch bản ngân sách tham khảo hiện tại là khoảng',
'XJTLU gợi ý dự trù khoảng 2.000 RMB/năm hoặc 1.000 RMB/học kỳ':'Nên dự trù khoảng 2.000 RMB/năm hoặc 1.000 RMB/học kỳ',
'Hướng dẫn ngân sách của XJTLU nêu ví dụ phí visa 400 RMB':'Có thể dự trù khoảng 400 RMB cho phí visa theo mức tham khảo hiện tại'
},
'xjtlu-ky-tuc-xa-sip-taicang.html':{
'Hướng dẫn pre-arrival hiện tại yêu cầu sinh viên XEC thanh toán toàn bộ tiền thuê bằng chuyển khoản trước khi đến Trung Quốc.':'Sinh viên XEC cần thanh toán toàn bộ tiền thuê bằng chuyển khoản trước khi đến Trung Quốc; nên chừa 2–3 tuần để xử lý.'
}
}

for fn,items in FAQ.items():
    p=Path(fn); s=p.read_text(encoding='utf-8')
    for a,b in REPL.get(fn,{}).items(): s=s.replace(a,b)
    if 'VISIBLE-FAQ-20260909' not in s:
        details=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)
        block=f'<!-- VISIBLE-FAQ-20260909 --><section class="section faq"><h2>Câu hỏi thường gặp</h2>{details}</section>'
        marker='<section class="section"><h2>Xem tiếp</h2>'
        assert marker in s,fn
        s=s.replace(marker,block+marker,1)
    # JSON-LD FAQ text must be reflected visibly.
    for q,_ in items: assert q in s, (fn,q)
    p.write_text(s,encoding='utf-8')
print('polished',len(FAQ),'Vietnam-market guides')

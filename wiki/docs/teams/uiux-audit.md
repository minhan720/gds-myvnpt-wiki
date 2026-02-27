---
hide:
  - toc
---
# 🔍 Đội Kiểm Định UI/UX (UIUX Audit Team)

## 🎯 Mục Tiêu
Phụ trách công tác rà soát, thẩm định luồng UI/UX trên nền tảng Figma trước khi tiến hành bàn giao (Handoff). Phân bổ nguồn lực rà soát để tối ưu hóa nhận thức người dùng (Cognitive Load), xử lý đa diện kịch bản lỗi (Edge Cases) và thống nhất UX Writing cho toàn dự án.

## 👥 Vai Trò Nhân Sự (Roles)
- **Lead Auditor (LA):** Chịu trách nhiệm phân bổ, bám sát các luồng chỉ đạo (JTBD). Tổng kết quy trình rà soát thành danh mục hành động điều chỉnh (Action Items) đệ trình cấp quản lý.
- **UX Evaluator (UXE):** Rà soát cấp độ Usability. Liên tục lược bỏ thông tin/giao diện dư thừa trên suốt thiết kế thao tác nhằm hạn chế rủi ro cho người dùng.
- **Edge Case Hunter (EC):** Mô phỏng rủi ro thực tế (Missing Connection, Empty State, Error State) khắc phục thiếu sót khi phát sinh bất thường hệ thống.
- **UI Analyst (UIA):** Kiểm duyệt tiêu chuẩn Visual UI. Giám sát sử dụng bảng màu, độ tương phản và thiết lập tỷ lệ (Spacing) đảm bảo đồng nhất Design System chuẩn WCAG.
- **UX Writer Auditor (UXW):** Thiết kế UX Writing. Cấu trúc lại cảnh báo, thông báo mã lỗi (404, Lỗi truy xuất) bằng ngôn ngữ hướng dẫn thân thiện và chuyên nghiệp.

## 🔄 Luồng Kiểm Định Có Hệ Thống (HITL Audit)
Hệ thống kết hợp kiểm tra điểm dừng xét duyệt của quản lý tại mỗi luồng (HITL - Human In The Loop) tối ưu tiến độ:

```text
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Phase 1   │   │   Phase 2   │   │   Phase 3   │
│  Lên Plan   │──▶│  Audit Figma│──▶│ Nghiệm Thu  │
└─────────────┘   └─────────────┘   └─────────────┘
  LA chốt JTBD     Team thao tác     LA Tổng Hợp
```

1. **[Lên Kế Hoạch - Phase 1]:** **LA** trích xuất bản đánh giá JTBD phân tích giới hạn Paint points người dùng yêu cầu kiểm soát. -> **Đệ trình xem xét Kế Hoạch Đánh Giá (Lần 1).**
2. **[Thực Hiện Kiểm Định - Phase 2]:** Khối chuyên trách (UXE, EC, UIA, UXW) đối soát trực tiếp lỗi trên thiết kế Frame. Các lỗi được nhãn hóa theo tình trạng báo động: Đỏ (Nghiêm trọng) - Cam (Khá nghiêm trọng) - Vàng (Cảnh báo).
3. **[Nghiệm Thu Báo Cáo - Phase 3]:** **LA** thống kê kết xuất mảng danh sách Action Items. **Đệ trình báo cáo File Audit [Mã Luồng] (Lần 2) phục vụ bộ phận thiết kế căn chỉnh.**

## 💡 Hướng Dẫn Kích Hoạt (Prompting)
Kích hoạt quy trình Audit chéo qua thiết lập lệnh mẫu:
> *"Yêu cầu `uiux-audit-team` áp dụng hệ thống HITL nhằm đánh giá bản thiết kế Figma sau: [Link Figma]. Mục tiêu chính tập trung quản lý Edge Cases, giảm tải nhận thức (Cognitive Load) và rà soát hiệu năng ngôn ngữ UX Writing. LA phân phối nhiệm vụ xuất bản báo cáo Markdown đầy đủ để chờ duyệt."*

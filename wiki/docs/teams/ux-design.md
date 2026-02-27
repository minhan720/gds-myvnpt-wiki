# ✏️ Đội Thiết Kế Trải Nghiệm & Sản Phẩm (UX Design Team)

## 🎯 Mục Tiêu
Tiến hành nghiên cứu, định vị hành vi người sử dụng thông qua Jobs-to-be-done (JTBD), hoàn thiện biểu đồ kiến trúc hệ thống (User Flows/Flowcharts) và xuất xưởng tài liệu Tech/Product Specs theo chuẩn Design Thinking phục vụ phát triển kỹ thuật.

## 👥 Vai Trò Nhân Sự (Roles)
- **Project Manager (PM):** Đầu mối quản trị dự án chung. Tiến hành khai thác đầu bài, phân công nhiệm vụ, quản lý tiến độ, và chủ trì trình báo cáo duyệt (HITL) mỗi quy trình.
- **UX Researcher (UR):** Tiếp nhận yêu cầu mảng thị trường (`Empathize & Define`). Thuyết minh rà soát JTBD, tổng hợp Pain Points phục vụ thông tin Insight cơ sở.
- **UX Designer (UX):** Thiết lập cấu trúc hệ thống (`Ideate & Prototype`). Diễn tả giải pháp của kiến trúc hệ thống thông qua thành phẩm Flowcharts mạch lạc dựa vào bản Insight chuyển nhượng.
- **Technical Writer (TW):** Phụ trách mô tả đặc tính kỹ thuật thông tin. Tổ hợp Flowcharts lập nên Tech Specs cho Developer, kết hợp rà soát thông điệp ngôn ngữ tương tác (UX Writing).
- **Quality Reviewer (CR):** Cấp kiểm duyệt chất lượng. Kiểm tra logic và mức độ sát sườn JTBD của kiến trúc, đảm bảo tuân thủ cấu trúc rẽ nhánh chuẩn yếu tố phân rã (MECE).

## 🔄 Luồng Vận Hành Khép Kín (HITL Workflow)
Toàn bộ chu trình sẽ tuân thủ cơ chế giải quyết báo cáo theo từng chặng quản trị trực tiếp từ quản lý (HITL - Human In The Loop) để hạn chế lỗi lệch hướng:

```text
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Gate 1    │   │   Gate 2    │   │   Gate 3    │   │  End-Game   │
│  Khởi Tạo   │──▶│ Thiết Kế UX │──▶│ Đặc Tả Specs│──▶│ Đóng Gói KB │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
  PM giao UR        UX vẽ Flow      TW viết Specs       PM Verify   
```

1. **[Gate 1 - Khởi tạo]:** **PM** gán việc truy xuất Insight đến **UR**. Hoàn thiện lập file phân tích và -> **Đệ trình quản lý chốt duyệt (Lần 1).**
2. **[Gate 2 - Thiết kế UX Flow]:** Phụ thuộc hệ Insight sẵn, **UX** xây dựng mạng Flowcharts, có cấp rà soát của bộ phận **CR**. -> **Báo cáo mô hình cấu trúc luồng (Lần 2).**
3. **[Gate 3 - Đặc tả & UX Writing]:** **TW** phân tích Flowcharts thành Technical Specs và UX Writing, đồng hành cùng kiểm thử logic từ **CR**. -> **Kiểm duyệt bản bàn giao tài liệu hoàn thiện cuối cùng (Lần 3).**
4. **[End-Game - Đóng Gói]:** **PM** tổng kết hạng mục và lập lưu trữ bản phát hành chung vào hệ thống `knowledge base` nhằm hoàn thiện phân phối thông tin nền tảng.

## 💡 Hướng Dẫn Kích Hoạt (Prompting)
Truy xuất nhanh yêu cầu qua kịch bản gọi chuẩn xác:
> *"Điều động team `ux-design-team` phục vụ phân tích dự án hạng mục [Ví dụ: Đăng ký dịch vụ eKYC MyVNPT]. Triển khai đầy đủ mô hình PM -> UR -> UX -> TW -> CR phục vụ rà soát JTBD, dựng màn Flowcharts chuẩn Spec. Đề nghị luồng có sử dụng rà soát HITL để cấp quyền xác nhận qua từng Gate!"*

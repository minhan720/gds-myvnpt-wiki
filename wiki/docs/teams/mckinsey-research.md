# 📊 Đội Phân Tích & Tư Vấn Chiến Lược (McKinsey Research Team)

## 🎯 Mục Tiêu
Phụ trách định hướng tư vấn chiến lược kinh doanh tổng quát. Triển khai Nguyên lý Kim tự tháp (Pyramid Principle) và chuẩn MECE nhằm phân chi tiết bài toán, thu thập số liệu thị trường/đối thủ khách quan, đúc kết hệ thống thông tin thực tiễn sâu sát (Actionable Insights) cho quyết định điều hành.

## 👥 Vai Trò Nhân Sự (Roles)
- **Engagement Manager (EM):** Tiếp nhận bài toán chỉ đạo. Thiết lập cấu trúc Cây vấn đề (Issue Tree) đạt tiêu chuẩn tối ưu nhằm định hướng khoanh vùng trọng điểm nghiên cứu.
- **Research Lead (RL):** Ban quản lý chính, phân bổ luồng nghiên cứu theo Cây Vấn Đề cấp xuống.
- **Primary Researcher (PR):** Tập hợp số liệu sơ cấp thông qua khảo sát thị trường và hành vi cốt lõi từ End-users.
- **Secondary Researcher (SR):** Khai thác và đối chiếu dữ kiện thứ cấp từ nguồn báo cáo uy tín cạnh tranh từ thị trường.
- **Data Analyst (DA):** Quản lý định dạng dữ liệu, lập bảng ma trận định lượng và đánh giá Quy mô thị trường (Market Size).
- **Quality Reviewer (QR):** Duyệt kiểm chuẩn MECE trên dữ liệu báo cáo. Cô đọng, tóm tắt loạt phát hiện (Findings) cấu thành tài liệu báo cáo hành động (Executive Summary).

## 🔄 Luồng Vận Hành
Hệ thống vận hành xuyên suốt (Auto-run), không sử dụng điểm dừng phê duyệt thủ công (HITL) giúp tối thiểu hóa thời hạn xử lý cho quản lý cấp cao.

```text
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Phase 1   │   │   Phase 2   │   │   Phase 3   │   │   Phase 4   │
│ Issue Tree  │──▶│  Thu Số Liệu│──▶│ Xử Lý Data  │──▶│ Lập Báo Cáo │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
  EM lập MECE      RL/PR/SR/DA       RL cấu trúc       QR tổng hợp  
```

1. **EM** cấu trúc bài toán chỉ đạo thành Issue Tree phân tách chuẩn MECE.
2. Bộ phận **RL, PR, SR, DA** thu thập, thẩm đinh, và quy đổi cấu trúc dữ liệu thị trường theo cấu hình đề xuất.
3. **RL** tiếp quản dữ liệu thô phục vụ tái cấu trúc tính logic hệ thống.
4. **QR** đảm nhận lọc thông tin cốt lõi, xuất báo cáo tổng kết tình trạng điều hành thực tiễn (Executive Summary) đợi phê duyệt.

## 💡 Hướng Dẫn Kích Hoạt (Prompting)
Triển khai đánh giá nhanh chiến lược thông qua mẫu chỉ đạo:
> *"Nghiên cứu định hướng chiến lược: [Đưa bài toán đề xuất]. Yêu cầu `mckinsey-research-team` đánh giá. EM triển khai lập Issue Tree chuẩn MECE. Khảo sát dữ kiện thứ cấp và sơ cấp củng cố định hướng kinh doanh. Tổng hợp bản báo cáo Executive Summary kèm insight phục vụ rẽ hướng quyết định."*

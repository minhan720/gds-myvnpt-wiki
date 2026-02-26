# [Tên Tính năng / Tên Dự án]
**Phiên bản (Version):** v1.0
**Ngày bắt đầu:** DD/MM/YYYY
**Người làm (Owner):** [Tên Agent/Người phụ trách]

---

## Phần I: Bối cảnh & Mục tiêu (Business Perspective)
- **Mục tiêu kinh doanh (Business Goals):** (Cải thiện số lượng user, tỷ lệ chuyển đổi, giảm lỗi, tăng doanh thu, v.v.)
- **Lộ trình triển khai (Rollout Plan):** 
  - (Ví dụ: Test nội bộ từ ngày X -> Public ngày Y)

---

## Phần II: Trải nghiệm Người dùng (UX & Copywriting)
- **User Stories (Hành trình):** 
  - Là một [đối tượng], tôi muốn [hành động] để giải quyết [nỗi đau/mục tiêu].
- **Sơ đồ UX (User Flow / Wireframe):** 
  - *(Chèn Mermaid chart hoặc link thiết kế Figma tại đây)*
- **Copywriting (Nội dung thấu cảm):**
  - Thông báo lỗi mạng/hệ thống: (Viết mềm mỏng)
  - Thông báo thành công: (Viết có cảm xúc/khen thưởng)
  - Tên nút bấm (CTA): (Nổi bật, rõ ràng hành động)

---

## Phần III: Quy trình & UI Logic (Step-by-step)
| Bước | Màn hình | Hành động của người dùng (User Action) | Phản hồi của hệ thống (System Response / UI Changes) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Phần IV: Đặc tả Nghiệp vụ & Kỹ thuật (Backend Logic)
- **Luật kinh doanh (Business Rules):** 
  - (Điều kiện áp dụng, đối tượng, phân khúc, thời hạn...)
- **Quy tắc máy tính (Logic Rule / Algorithm):** 
  - (Tỷ lệ quy đổi, xác suất ngẫu nhiên, giới hạn số lần thao tác...)
- **Xử lý Ngoại lệ (Edge Cases / Exception Handling):** 
  - (Nếu giao dịch mất mạng giữa chừng, hết số dư, API bên thứ 3 chết thì sao?)
- **Tác vụ ngầm (Background Jobs / Cronjobs):** 
  - (Ví dụ: 0h sáng quét dữ liệu, sau 30p không thanh toán thì hủy đơn...)

---

## Phần V: Kiểm thử & Vận hành (Testing/Operation)
- **Kịch bản Test (Test Scenarios):** 
  - (Các luồng chính cần pass QA, luồng âm...)
- **Cấu hình CMS/Admin:** 
  - (Các tham số trên Portal Admin có thể bật tắt/chỉnh thông số mà không cần code lại)
- **Tracking & Analytics:** 
  - (Gắn thẻ ở các nút bấm nào, đếm tỷ lệ rời bỏ ở màn hình nào?)

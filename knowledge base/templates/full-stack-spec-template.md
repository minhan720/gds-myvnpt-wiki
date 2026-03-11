# [Tên Tính năng / Tên Dự án]
- **Link Google Docs:** [full-stack-spec-template](https://docs.google.com/document/d/1KiQFH6M9aK8SEMWRFgFGdhLvahBs7JCTY1mYe1EVo2w/edit)
**Phiên bản (Version):** v1.0
**Ngày bắt đầu:** DD/MM/YYYY
**Người làm (Owner):** [Tên Agent/Người phụ trách]

---

## Phần I: Bối cảnh & Mục tiêu (Business Perspective)
- **Mục tiêu kinh doanh (Business Goals):** (Cải thiện số lượng user, tỷ lệ chuyển đổi, giảm lỗi, tăng doanh thu, v.v.)
- **Lộ trình triển khai (Rollout Plan):** 
  - (Ví dụ: Test nội bộ từ ngày X -> Public ngày Y)

---

## Phần II: Đo lường & Chỉ số (Metrics)
- **Cơ chế đo lường (Measurement mechanism):** (Sử dụng Tool gì? Firebase, SQL, Google Analytics, Logs...)
- **Chỉ số Bắc đẩu (North star):** (Chỉ số duy nhất quan trọng hàng đầu cho tính năng này)
- **Chỉ số Thành công (Success metrics):** (Các Kpis cụ thể cần đạt được)
- **Các chỉ số khác (Other metrics):** (Các chỉ số phụ hỗ trợ theo dõi hành vi)
- **Chỉ số Rào chắn / Duy trì (Guardrail / Maintain):** (Chỉ số để đảm bảo tính năng không gây phản tác dụng cho hệ thống chung)
- **Tracking & Analytics:** (Gắn thẻ ở các nút bấm nào, đếm tỷ lệ rời bỏ ở màn hình nào?)

---

## Phần III: Trải nghiệm Người dùng (UX & Copywriting)
- **User Stories (Hành trình):** 
  - Là một [đối tượng], tôi muốn [hành động] để giải quyết [nỗi đau/mục tiêu].
- **Sơ đồ UX (User Flow / Wireframe):** 
  - *(Chèn Mermaid chart hoặc link thiết kế Figma tại đây)*
- **Copywriting (Nội dung thấu cảm):**
  - Thông báo lỗi mạng/hệ thống: (Viết mềm mỏng)
  - Thông báo thành công: (Viết có cảm xúc/khen thưởng)
  - Tên nút bấm (CTA): (Nổi bật, rõ ràng hành động)

---

## Phần IV: Quy trình & Đặc tả Kỹ thuật (Master Flow & Logic)
| Bước | Mã màn hình | Giao diện | Điểm chạm (Touch-point) | Hành động (User Action) | Phản hồi Hệ thống & UI (System/UI Response) | Quy tắc nghiệp vụ & Logic (Backend/Logic Rules) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

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


<!-- gdoc_id: 1KiQFH6M9aK8SEMWRFgFGdhLvahBs7JCTY1mYe1EVo2w -->

# UI/UX Audit Team Workflow (Mandatory HITL)

## Giới thiệu
Tổ hợp `uiux-audit-team` chuyên thực hiện việc đọc hiểu thiết kế UI/UX qua nội dung Figma, phân tích luồng cognitive flow của người dùng, rà soát Edge Cases, kiểm định microcopy và Accessibility. 
Đầu ra cuối cùng là một bản báo cáo `Audit_*.md` tổng hợp chi tiết lỗi và các Action Items.

**Mô hình vận hành: Human-in-The-Loop (HITL)**
Tất cả các mốc chuyển giao công việc hoặc ra quyết định cốt lõi đều phải có sự xác nhận của Boss (Human). Trưởng nhóm kiểm định (LA - Lead Auditor) không được tự ý đi tiếp nếu không có `>>> Approved`.

## Các vai trò (Roles)
1. **LA (Lead Auditor)**
   - Trưởng nhóm, đánh giá góc nhìn Business và JTBD.
   - Quản lý các mốc trình Boss duyệt. Tổng hợp lỗi.
2. **UXE (UX Examiner)**
   - Phân tích luồng thao tác. Định vị các nút thắt nhận thức (cognitive load).
3. **EC (Edge Case Engineer)**
   - Tìm kiếm các luồng người dùng thiểu số hoặc các trường hợp lỗi (Error State, Empty State).
4. **UIA (UI Auditor)**
   - Đánh giá thị giác, độ tương phản (contrast), khoảng cách (spacing), tuân thủ WCAG.
5. **UXW (UX Writer)**
   - Rà soát lời văn (microcopy), tinh chỉnh cho tự nhiên và dễ định hướng.

## Quy trình Kiểm định (Mandatory HITL Sequence)

* **GIAI ĐOẠN 1: TIỀN PHÂN TÍCH VÀ ĐỊNH VỊ JTBD**
  1. **Bước 1 (Boss → LA)**: Boss cung cấp link Figma hoặc tài liệu Scope cho LA qua prefix `>>> `.
  2. **Bước 2 (LA)**: LA dùng Figma MCP đọc cấu trúc file, lên Draft ngắn xác định:
     - *Main JTBD*: Luồng này sinh ra để người dùng giải quyết job gì?
     - *Pain point*: Khách sợ nhất gì khi làm job này?
  3. **Bước 3 (LA → 🛑 BOSS DUYỆT LẦN 1)**: LA nộp Draft. Kêu gọi Boss duyệt (`>>> Review Required at [Nội dung Draft]`).
     - *Boss `>>> Reject`*: LA phải tự phân tích lại.
     - *Boss `>>> Approved`*: LA đi tiếp Bước 4.

* **GIAI ĐOẠN 2: CHUYÊN GIA SOI LỖI (AUDIT)**
  4. **Bước 4 (LA → UXE, EC, UIA, UXW)**: Giao task. Chuyển JTBD đã chốt làm "kim chỉ nam" cho dàn chuyên gia audit.
  5. **Bước 5 (Auditing phase)**: Cả 4 Agents đồng loạt kiểm tra màn hình và ghi nhận Findings (Lỗi/Điểm tốt), gán Severity (🔴 Critical, 🟠 Major, 🟡 Minor). Sau đó gửi lại cho LA.

* **GIAI ĐOẠN 3: TỔNG HỢP VÀ BÁO CÁO MỘT CỬA**
  6. **Bước 6 (LA)**: Gom toàn bộ Findings từ các Agent. Xóa những điểm trùng lặp. Sửa format markdown đẹp mắt ra file `Audit_[Tên_Luồng].md`. Có thể yêu cầu các Agent rà soát lại văn phong báo cáo (tiền kiểm) trước khi nộp.
  7. **Bước 7 (LA → 🛑 BOSS DUYỆT LẦN 2)**: Trình báo cáo cuối cùng cho Boss duyệt.
     - *Boss `>>> Approved`*: LA đóng Sprint Audit. 
     - *Nếu Boss yêu cầu bổ sung*: LA lại quay về Bước 4.

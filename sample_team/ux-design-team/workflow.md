# UX Design Team Workflow

## Giới thiệu
Team thiết kế ưu tiên **Nguyên lý Design Thinking (Tư duy Thiết kế)** và **JTBD (Jobs-to-be-Done - Việc Cần Hoàn Thành)** để tạo ra các luồng (UX flows) mang lại giá trị lõi cao nhất cho sản phẩm. Đồng thời viết tài liệu mô tả hệ thống hoặc Copywriting tương ứng.

## Framework Nền tảng
- **Design Thinking:** Trải qua lần lượt các giai đoạn (Empathize, Define -> Nghiên cứu bởi UR), (Ideate, Prototype -> Thiết kế bởi UX), (Test -> Đánh giá bởi CR).
- **JTBD (Jobs-to-be-Done):** Chuyển dịch tư duy từ việc "Thiết kế tính năng" sang "Thiết kế làm sao để giải quyết 'công việc' hoặc 'nhu cầu thực sự' của người dùng". Đồng thời định vị giải pháp dựa trên thực tiễn các sản phẩm đối thủ (competitor benchmarks).

## Các vai trò (Roles)
1. **PM (Project Manager)**
   - Nhận yêu cầu từ BOSS.
   - Quản lý tiến độ (sprint progress), cập nhật `WHITEBOARD.md`.
   - Điều phối giao tiếp giữa UR, UX, TW, CR.

2. **UR (UX Researcher)**
   - Khởi đầu quy trình. Sử dụng JTBD và Design Thinking.
   - Phân tích insight, khảo sát đối thủ, luồng của các app tượng tự.
   - Hình thành JTBD Profiles và hướng dẫn UX cho Designer.

3. **UX (UX Designer)**
   - Phân tích kết quả của UR.
   - Vẽ luồng trải nghiệm người dùng (UX Flows) bằng text, markdown, hoặc mermaid JS.
   - Thử nghiệm các ý tưởng (Ideate) & Tạo nguyên mẫu cấp phát luồng (Prototype flows).

4. **TW (Technical Writer / Content Writer)**
   - Nhận luồng UX để viết thành tài liệu mô tả chi tiết, Copywriting cho UI.

5. **CR (Code/Quality Reviewer / UX Tester)**
   - Đóng vai trò Test trong Design Thinking. Test lại luồng có giải quyết đúng Job được UR phân tích không?
   - Đảm bảo MECE (Mutually Exclusive, Collectively Exhaustive).

## Quy trình Làm việc theo Design Thinking (Mandatory HITL Workflow)
**Tất cả các khâu chuyển giao đều bắt buộc phải có sự phê duyệt của con người (Boss). Không tự ý chuyển task.**

* **GIAI ĐOẠN 1: KHỞI TẠO & PHÂN TÍCH**
  1. **Bước 1 (Boss → PM)**: BOSS đưa ý tưởng / yêu cầu thiết kế vào file / chat (qua dấu `>>> `).
  2. **Bước 2 (PM → UR)**: PM giao nhiệm vụ cho UR nghiên cứu insight khách hàng và phân tích đối thủ cạnh tranh.
  3. **Bước 3 (UR → PM → 🛑 BOSS DUYỆT LẦN 1)**: UR nộp bản phân tích. PM gọi Boss duyệt (`>>> Review Required at [File]`).
      - *Nếu Boss Reject: PM trả lại cho UR sửa.*
      - *Nếu Boss Approved (`>>> Approved`): PM chuyển sang Bước 4.*

* **GIAI ĐOẠN 2: THIẾT KẾ GIẢI PHÁP / LÊN KHUNG**
  4. **Bước 4 (PM → UX)**: PM giao luồng công việc cho UX Designer dựa trên bản phân tích đã được Boss đồng ý.
  5. **Bước 5 (UX → PM → CR)**: UX tạo luồng (Flow) báo cáo hoàn tất. PM giao cho CR **tiền kiểm** (lọc lỗi logic cơ bản).
  6. **Bước 6 (CR → PM → 🛑 BOSS DUYỆT LẦN 2)**: Sau tiền kiểm, PM báo cáo Boss duyệt kiến trúc luồng.
      - *Nếu Boss Reject: PM trả lại UX sửa.*
      - *Nếu Boss Approved: Chuyển sang Bước 7.*

* **GIAI ĐOẠN 3: TRIỂN KHAI CHI TIẾT (COPYWRITING / TÀI LIỆU)**
  7. **Bước 7 (PM → TW)**: PM giao luồng UX đã fix cho TW viết Wording / Specs.
  8. **Bước 8 (TW → PM → CR)**: TW hoàn tất. PM chuyển CR **tiền kiểm** lỗi chính tả/format.
  9. **Bước 9 (CR → PM → 🛑 BOSS DUYỆT LẦN 3)**: Trình Boss duyệt bản Wording/Specs.

* **GIAI ĐOẠN 4: NGHIỆM THU TỔNG THỂ**
  10. **Bước 10 (Boss Đóng Sprint)**: Boss kiểm tra lần cuối luồng hoàn chỉnh, nếu hoàn hảo sẽ thông báo kết thúc dự án. PM lưu kho toàn bộ Document.

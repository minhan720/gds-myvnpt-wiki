# Lệnh Thực Thi: ÁNH XẠ COMPONENT & TẠO TRANG TÀI LIỆU CHI TIẾT

## MỤC TIÊU
Dùng MCP quét Component cụ thể từ Figma, viết code UI Component chuẩn mực và tạo trang tài liệu (Docs Page) chi tiết cho nó.

## CẤU TRÚC TRANG & XỬ LÝ VISUAL (BẮT BUỘC TUÂN THỦ 100%)
**Cụ thể, mỗi trang Component CHỈ ĐƯỢC BAO GỒM các phần (Sections) sau theo đúng thứ tự:**

1. **Page Header (Tiêu đề & Phụ đề):**
   - Tên Component (H1 lớn, font-bold).
   - Một câu mô tả ngắn gọn (Description) ngay bên dưới.

2. **Visual Preview (Khu vực Hiển thị / Demo):**
   - Đây là phần quan trọng nhất. Ngươi phải tạo một Box/Card hiển thị giao diện thực tế của Component (ví dụ: Button, Card) căn giữa (center-aligned).
   - Component bên trong phải hiển thị chính xác dựa trên Design Tokens đã quét, không bị méo hoặc vỡ layout.

3. **Usage / Code Snippet (Đoạn mã sử dụng):**
   - Đặt ngay dưới phần Preview.
   - Cung cấp một khối code (Code Block) định dạng syntax highlighting đúng chuẩn.
   - Có nút "Copy" ở góc trên cùng bên phải của khối code

4. **API Reference / Props Table (Bảng thuộc tính):**
   - Hiển thị danh sách các Variants (Primary, Secondary) và Props dưới dạng bảng (Table) đơn giản, viền mảnh, font chữ rõ ràng.

5. **⚠️ Cảnh báo Edge Cases / Accessibility:**
   - Liệt kê các giới hạn, trạng thái lỗi hoặc quy tắc thiết kế rủi ro (Resilience Design) đã định nghĩa trong file hệ thống.

**🚫 LỆNH CẤM KHI XỬ LÝ VISUAL:**
- KHÔNG thêm các hiệu ứng rườm rà (animation phức tạp, màu sắc lòe loẹt) nếu trang mẫu không có.
- KHÔNG tự ý chèn thêm các Section rác (như Lịch sử phát triển, Thông tin ngoài lề).
- Giao diện phải đi theo triết lý "Minimalist & Clean"

## QUY TRÌNH THỰC THI (Tuân thủ nghiêm ngặt)

1. **Quét Figma & Code Component (Base Code):**
   - Bắt đầu với các component nhỏ nhất trước (ví dụ: Button, Input, Card, Badge).
   - Đọc link Figma được cung cấp qua MCP để lấy thông số chính xác.
   - Code component bằng React/Tailwind. Sử dụng TypeScript interface để đảm bảo tính chặt chẽ cho mọi props của component.
   - Khi cần tính năng mới, phải kiểm tra xem có thể tạo thành component dùng chung không.

2. **Xây dựng Trang Tài liệu Component (Component Page Assembly):**
   - Lắp ghép các UI Components đã tạo vào trang tài liệu chi tiết.
   - Mỗi trang component BẮT BUỘC phải có đầy đủ 5 phần sau theo thứ tự:
     1. **Tổng quan (Overview):** Đoạn mô tả ngắn gọn về tác dụng của component.
     2. **Biến thể (Variants):** Bảng hiển thị các trạng thái (Primary, Secondary, Disabled,...) và Props tương ứng.
     3. **Hướng dẫn sử dụng (Usage Guidelines):** Khi nào nên dùng, khi nào KHÔNG nên dùng component này.
     4. **Khả năng tiếp cận (Accessibility - a11y):** Các quy tắc về ARIA, focus state, contrast ratio.
     5. **Đoạn mã code (Code Snippets):** Block code chuẩn xác để lập trình viên có thể copy và sử dụng ngay.

3. **INTERACTIVE CHECKPOINT (BẮT BUỘC DỪNG LẠI):**
   - 🛑 KHÔNG tự ý chuyển sang component tiếp theo.
   - Hãy dừng lại và hỏi người dùng: *"Tôi đã tạo xong base code và cấu trúc Layout tài liệu cho component này dựa trên Figma. Bạn có muốn thêm Variant nào mà trong Figma có thể bị thiếu không, hoặc có muốn tôi tiếp tục generate cho các component khác không?"*
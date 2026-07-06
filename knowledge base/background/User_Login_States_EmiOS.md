# Quy hoạch Trạng thái Người dùng & Phương thức Đăng nhập (User Login States) - MyVNPT / EmiOS

Tài liệu này định nghĩa chi tiết các trạng thái phân tầng của người dùng (User States) trên MyVNPT (EmiOS) dựa trên mức độ định danh (KYC) và các phương thức đăng nhập tương ứng. Đây là cơ sở để thiết kế các luồng UX/UI theo hướng cá nhân hóa và loại bỏ các rào cản tiếp cận (Login Wall).

## 1. Chuyển dịch Cốt lõi: Từ "Thuê bao" sang "Chủ thể con người"

Thay vì quản lý tài khoản dựa trên Số điện thoại (Subscriber-centric), hệ sinh thái EmiOS chuyển sang quản lý theo **Chủ thể con người (Customer-centric)** thông qua **VNPT Digital ID** (gắn với CCCD/CMND). 
Số điện thoại (dù nội mạng hay ngoại mạng) và Tài khoản MXH (Social Login) chỉ được xem là các **Phương thức Đăng nhập (Login Methods)**. Mục tiêu của hệ thống (Backend/CDP) là hợp nhất tất cả các phương thức này về chung một định danh con người duy nhất.

---

## 2. Bức tranh toàn cảnh 6 Trạng thái User (User States Journey)

Hành trình của một người dùng từ lúc mới biết đến App (người lạ) cho đến khi trở thành "Công dân số VIP" được chia thành 6 trạng thái (State) đi qua các lớp phễu:

### State 0: Khách Khám phá Ẩn danh (Anonymous Explorer)
*   **Đầu vào:** Tải app và mở lên, **không cần đăng nhập**. Hệ thống ghi nhận theo Device ID.
*   **Đặc điểm:** Trải nghiệm "Window Shopping" (Đi dạo mua sắm). Nhằm xóa bỏ hoàn toàn áp lực "Login Wall".
*   **Quyền hạn:** Thoải mái lướt xem phân hệ DigiShop (kho SIM, thiết bị, gói cước), đọc tin tức, xem khuyến mãi...
*   **Điểm chặn (Login Wall):** App chỉ yêu cầu đăng nhập khi khách hàng phát sinh giao dịch (Mua SIM, mua gói cước, mua thiết bị...) hoặc cố tình truy cập vào các tính năng bảo mật (Quản lý thiết bị nhà, Xem cước).

### State 4: Khách Vãng lai có tài khoản (Guest)
*   **Đầu vào:** Đăng nhập bằng SĐT ngoại mạng.
*   **Đặc điểm:** Đã cho hệ thống thông tin liên hệ, nhưng hệ thống chưa map được với bất kỳ tài sản/hợp đồng viễn thông nào của VNPT.
*   **Quyền hạn:** Có thể hoàn tất các giao dịch thương mại điện tử (DigiShop), theo dõi tiến độ đơn hàng. Các tính năng Customer Care không có quyền truy cập.

### State 3: Khách hàng Tiện ích chéo (Off-network Fixed-line Owner)
*   **Đầu vào:** Đăng nhập bằng SĐT ngoại mạng.
*   **Đặc điểm:** Hệ thống quét và thấy SĐT ngoại mạng này đang được dùng làm số liên hệ của một hợp đồng Internet Fiber/Camera VNPT ở nhà. Tuy nhiên, hợp đồng này chưa được map với "Định danh con người" (CCCD). Khách hàng này hoàn toàn có thể đang sở hữu ngầm 1 thuê bao VinaPhone khác mà App chưa quét ra được.
*   **Quyền hạn:** Giao diện tập trung vào quản lý dịch vụ Internet (DigiHome). Có thể báo hỏng mạng, đóng cước internet.
*   **Mục tiêu của Agent:** 
    *   **Ưu tiên 1 (Xác thực chéo - Cross-Auth):** Khuyến khích khách hàng thực hiện xác thực định danh (eKYC bằng CCCD) với lý do "để bảo mật hợp đồng Internet". Ngay khi có CCCD, hệ thống sẽ tự động map xem khách hàng có SĐT VinaPhone nào không để gom chung vào quản lý (chuyển thẳng lên State 1).
    *   **Ưu tiên 2 (Upsell):** Nếu eKYC xong mà vẫn chưa có sim VNP, Agent sẽ liên tục giới thiệu mua sim VinaPhone để ghép vào gói Home tận hưởng data dùng chung.

### State 2: Khách hàng VNPT - Thiếu/Sai thông tin (Unverified VNP - Edge case)
*   **Đầu vào:** Đăng nhập bằng SĐT VinaPhone.
*   **Đặc điểm:** Là thuê bao nội mạng nhưng hồ sơ đăng ký bị thiếu, sai lệch với CSDL Quốc gia. *(Lưu ý: Do chính sách bắt buộc chuẩn hóa thông tin thuê bao hiện nay, State này hầu như chỉ là các ngoại lệ (Edge case) hoặc phát sinh khi khách hàng cập nhật giấy tờ mới).*
*   **Quyền hạn (Hạn chế):** Đây là "Trạm kiểm soát an ninh". App sẽ khóa các tính năng nhạy cảm (ứng tiền, chuyển quyền) và kích hoạt luồng cảnh báo ưu tiên: *"Vui lòng chuẩn hóa thông tin thuê bao (eKYC)"*.

### State 1: Khách hàng Định danh Hoàn chỉnh (Fully Identified VNP)
*   **Đầu vào:** Vượt qua eKYC hoặc đăng nhập bằng SĐT VNP có hồ sơ chuẩn.
*   **Đặc điểm:** Khách hàng chính thức được cấp VNPT Digital ID (gắn chặt với CCCD). Mọi tài nguyên (từ đa SĐT, Internet, MyTV, điểm Loyalty) được hợp nhất.
*   **Quyền hạn:** Trạng thái "Công dân số VIP". Mở khóa 100% Hệ sinh thái (Không gian Cá nhân + Không gian Gia đình). Trợ lý Agent MyVNPT (Emi) phục vụ ở mức độ cá nhân hóa và chủ động cao nhất.

### State 5: Thành viên được Ủy quyền (Delegated Member)
*   **Đầu vào:** Bất kỳ SĐT nào.
*   **Đặc điểm:** Nhánh phụ song song. Khách hàng không trực tiếp đứng tên dịch vụ viễn thông, nhưng được người ở **State 1** (Chủ nhóm) mời vào Nhóm Gia đình.
*   **Quyền hạn:** Trải nghiệm App ở Không gian Nhóm (Group Workspace). Chỉ thao tác được trên các quyền hạn mà Chủ nhóm cấp (VD: Dùng chung data, xem camera phòng khách).

---

## 3. Quy hoạch Phương thức Đăng nhập (Login Methods)

Để dẫn dắt mượt mà khách hàng đi qua các State trên, MyVNPT cần cấu trúc các phương thức đăng nhập theo 3 cấp độ:

### 3.1. Nhóm Phương thức Cốt lõi (Bắt buộc)
*   **Đăng nhập Tự động qua 3G/4G (Zero-touch Login):** Tự động nhận diện mạng VinaPhone, cho khách hàng vào thẳng App không cần nhập số hay chờ OTP. Tạo trải nghiệm đặc quyền cao nhất.
*   **Đăng nhập bằng SĐT + Mã OTP:** Phục vụ mọi State. Gửi mã qua SMS hoặc Zalo ZNS.
*   **Đăng nhập bằng Mật khẩu tĩnh:** Phương án dự phòng (Fallback) khi khách hàng không nhận được OTP (VD: đang ở nước ngoài).

### 3.2. Nhóm Phương thức Thu hút & Tiện lợi (Growth & Convenience)
*   **Đăng nhập qua Mạng xã hội (Apple/Google/Facebook):** Giảm ma sát đầu vào cho khách vãng lai ở State 4. Hỗ trợ bắt "leads" cực tốt cho DigiShop.
*   **Đăng nhập bằng Sinh trắc học thiết bị (FaceID/TouchID):** Tiện lợi cho người dùng mở app hàng ngày, phục vụ tốt cho các luồng xác thực thanh toán, tích điểm.

### 3.3. Nhóm Phương thức Chiến lược (Strategic & Ecosystem)
*   **Đăng nhập qua VNeID:** "Vũ khí hạng nặng". Xác thực thẳng qua CSDL Bộ Công An. Khách hàng ngay lập tức có tập KYC "sạch 100%", đẩy thẳng họ vào State 1 (Định danh hoàn chỉnh) mà không cần qua các bước chuẩn hóa rườm rà.
*   **Đăng nhập quét mã QR (Cross-device):** Kết nối liền mạch giữa App và Web, hoặc App và TV (MyTV), hoàn thiện hệ sinh thái OMO (Online-Merge-Offline).

---

## 4. Các Chiến lược Thực thi UX Xuyên suốt

1.  **Giao diện Phân tầng (Progressive UI):** App tự động "co giãn" giao diện. Khách State 0 sẽ thấy App như một sàn Shopee bán SIM/Thiết bị. Khách State 1 sẽ thấy App là một Dashboard quản lý gia đình thông minh.
2.  **Hợp nhất Dữ liệu (Identity Merging):** Khi một khách hàng chuyển từ State 4 (ngoại mạng) sang State 1 (mua sim VNP và eKYC), hệ thống Backend phải tự động gộp (merge) toàn bộ điểm Loyalty, lịch sử đơn hàng cũ sang mã định danh mới.
3.  **Cross-selling bằng Agent:** Lợi dụng các State lỡ cỡ (như State 3) để Agent Emi giao tiếp chèo kéo khéo léo (Ví dụ: "Đằng nào cũng lắp WiFi, mua thêm sim VNP để dùng 30GB ké nhà bạn nhé").

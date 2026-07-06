# Tổng hợp Định hướng Chiến lược: Danh tính Người dùng & Concept Hộ gia đình

Để hiện thực hóa tầm nhìn chuyển đổi MyVNPT (EmiOS) thành một Trợ lý số thông minh, Concept sản phẩm mới được kiến tạo dựa trên hai trụ cột chiến lược cốt lõi: **(1) Quy hoạch lại Danh tính người dùng** (lấy con người làm trung tâm thay vì thuê bao) và **(2) Định hình Concept Hộ gia đình** (giải quyết triệt để bài toán quản lý chéo). Đây là hai nền tảng kiến trúc tiên quyết giúp phá bỏ rào cản tiếp cận, tạo ra trải nghiệm liền mạch và cá nhân hóa cho khách hàng.

## 1. Định hướng Quy hoạch Trạng thái Người dùng & Định danh số

Chiến lược này phá bỏ rào cản tiếp cận truyền thống nhằm tạo ra trải nghiệm cá nhân hóa liền mạch:

*   **Chuyển đổi cốt lõi "Lấy con người làm trung tâm" (Human-Centric):** Thay vì quản lý phân mảnh theo từng số điện thoại (Subscriber-centric), hệ thống chuyển sang định danh duy nhất bằng **VNPT Digital ID** (được đối chiếu và gắn liền với CCCD/CMND). Các yếu tố như số điện thoại (nội/ngoại mạng) hay tài khoản mạng xã hội giờ đây chỉ đóng vai trò là "Phương thức đăng nhập" (Login Methods). Sự dịch chuyển này giúp hợp nhất toàn bộ tài sản số (nhiều thuê bao di động, internet, truyền hình, điểm thưởng...) của khách hàng về chung một hồ sơ duy nhất. Từ đó, hệ thống nhận diện chính xác "Bạn là ai" thay vì "Bạn đang dùng số nào", mở đường cho một trải nghiệm chăm sóc và cá nhân hóa sâu sắc nhất.
*   **Hành trình 6 Trạng thái & Giao diện "Co giãn":** Bỏ rào cản đăng nhập ban đầu (Login Wall), hệ thống phân loại khách hàng từ *Khách ẩn danh* đến *Khách định danh hoàn chỉnh*. Ứng với mỗi trạng thái, giao diện MyVNPT sẽ tự động thay đổi: người dùng ẩn danh trải nghiệm App như một cửa hàng (DigiShop), trong khi khách VIP sở hữu bảng điều khiển (Dashboard) quản lý toàn diện với kịch bản tương tác và quyền hạn tối đa.
*   **Đăng nhập Không ma sát:** Triển khai đa dạng phương thức đăng nhập: Nhóm Cốt lõi (3G/4G tự động, OTP), Nhóm Tiện lợi (Sinh trắc học, Social Login) và Nhóm Chiến lược (VNeID, QR Code), tối ưu hóa trải nghiệm cho từng phân khúc.

## 2. Quy hoạch Kiến trúc Thực thể & Concept Hộ gia đình

MyVNPT giải quyết bài toán quản lý tiện ích dùng chung bằng cách thiết lập các "Không gian Nhóm/Gia đình", xoay quanh 4 nguyên tắc:

*   **Không gian ảo (Virtual Workspace) đa vai trò:** Một người dùng có thể linh hoạt tham gia nhiều nhóm với cấu trúc Nhiều-Nhiều (N-N). Họ có thể là "Chủ nhóm" (trả tiền cước) ở gia đình mình, nhưng là "Thành viên" (dùng chung data) ở một nhóm khác.
*   **Ủy quyền minh bạch (Delegation):** Tách bạch rõ ràng *Quyền sở hữu* và *Quyền quản lý*. Chủ nhóm không thể tự ý can thiệp vào thuê bao thành viên nếu chưa gửi yêu cầu và được "Xác nhận đồng ý" nhằm bảo vệ quyền riêng tư tuyệt đối.
*   **Thao tác hộ (Proxy Actions):** Khi được ủy quyền, Chủ nhóm đóng vai trò như "quản gia", có thể thực hiện nghiệp vụ thay thành viên: *Tra cứu* (cước, data), *Hành động* (thanh toán, mua gói) và *Hỗ trợ* (báo hỏng).
*   **Chuyển đổi ngữ cảnh (Context Switcher):** UX/UI cho phép chuyển đổi tức thì giữa *Không gian Cá nhân* và *Không gian Gia đình*. Hệ thống thông báo (Notifications) cũng được phân luồng riêng biệt để tránh rác thông tin (spam) giữa các vai trò.

# Quy hoạch hiển thị: Widget và Feeds trên màn hình Home

Tài liệu này mô tả chi tiết về quy hoạch, định hướng phát triển cũng như phương thức hiển thị cho 2 nhóm truyền thông cốt lõi trên màn hình Home MyVNPT: **Widget** và **Feeds**.

Hai nhóm này đóng vai trò như "hai nửa bán cầu não" của ứng dụng: Widget là não trái (logic, cá nhân, quản lý tài sản), còn Feeds là não phải (cảm xúc, khám phá, giao tiếp cộng đồng).

---

## 1. Nhóm WIDGET: Khung tiếp cận "Widget-Driven" và Giao diện Phân tầng

Đây là khu vực "đất vàng" trên màn hình Home. Tại MyVNPT, chúng ta áp dụng tư duy **"Widget-Driven Design"**: Mỗi tính năng từ nay về sau khi được tích hợp trên App đều phải đi kèm với một thiết kế Widget. Tính năng không được "giấu" sâu trong menu mà phải có khả năng "trồi" lên bề mặt Home screen dưới dạng các điểm chạm (touchpoints).

Đồng thời, áp dụng nguyên tắc **Giao diện Phân tầng (Progressive UI)**, hệ thống Widget được chia thành 2 nhóm lớn và có luật hiển thị khác nhau dựa trên Trạng thái người dùng (User Login States).

### A. Phân loại Widget và Luật hiển thị (Dynamic Layouts)

#### Nhóm 1: Acquisition & Growth Widgets (Widget Thu hút & Tăng trưởng)
*   **Bản chất:** Đóng vai trò như các Banner/Shortcut mua sắm động.
*   **Mục tiêu:** Chuyển đổi khách Ẩn danh/Vãng lai thành Khách hàng VNP (Acquisition), hoặc bán chéo (Cross-sell).
*   **Ví dụ:** Mời Chuyển mạng giữ số (MNP), Chọn SIM số đẹp, Đăng ký lắp đặt WiFi, Mua gói Data ngày.
*   **Luật hiển thị:** 
    *   **Hiển thị 100% không gian Home** đối với **User State 0 (Ẩn danh)** và **State 4 (Vãng lai)**. Thay thế hoàn toàn các widget dịch vụ bị khóa.
    *   Hiển thị đan xen đối với **User State 3 (Chỉ dùng Internet)** để bán chéo dịch vụ Di động.
    *   **Ẩn đi (hoặc đẩy xuống Feeds)** đối với **User State 1 (Định danh chuẩn)** để trả lại không gian quản trị sạch sẽ.

#### Nhóm 2: Operation & Care Widgets (Widget Quản trị & Chăm sóc)
*   **Bản chất:** Bảng điều khiển (Dashboard) phản ánh sức khỏe tài sản số.
*   **Mục tiêu:** Giữ chân (Retention), Quản trị cá nhân hóa, Tự phục vụ (Self-service).
*   **Ví dụ:** Quản lý Data, Theo dõi Cước, Trạng thái Camera/Internet, Lịch hẹn Kỹ thuật viên.
*   **Luật hiển thị:**
    *   **Tuyệt đối Ẩn** với User State 0 và 4 (để tránh hiển thị trạng thái "Bị khóa" gây trải nghiệm xấu).
    *   Hiển thị theo đúng dịch vụ thực tế mà User State 1, 3, 5 đang sở hữu.

### B. 5 Trạng thái Vòng đời của một Widget (5 Lifecycle States)

Khi một Widget đã **đủ điều kiện hiển thị** trên màn hình, PO phải thiết kế nó đi qua 5 trạng thái vòng đời sau để giao tiếp hiệu quả với khách hàng:

1.  **Empty / Setup State (Trạng thái Rỗng / Mời thiết lập):**
    *   *Sử dụng khi:* Khách có quyền dùng nhưng chưa thiết lập dữ liệu ban đầu.
    *   *Ví dụ:* "Bạn chưa liên kết mã khách hàng. Thêm hóa đơn Điện/Nước để theo dõi hàng tháng." -> `[Nút: Thêm hóa đơn]`.
2.  **Normal / Zero-State (Trạng thái Bình thường / Yên bình):**
    *   *Sử dụng khi:* Dịch vụ đang ổn định, không rủi ro. Thiết kế màu trung tính, dịu mắt (Quiet UI).
    *   *Ví dụ:* "Lưu lượng còn 4.5 GB. Tốc độ cao."
3.  **Alert / Action-Required (Trạng thái Cảnh báo khẩn):**
    *   *Sử dụng khi:* Có rủi ro ngắt dịch vụ hoặc **rủi ro pháp lý (eKYC)**. Widget đổi màu Đỏ/Cam, tự động phình to kích thước.
    *   *Ví dụ (Tuân thủ):* "CẢNH BÁO: Thuê bao chưa chuẩn hóa thông tin. Cập nhật ngay để không bị khóa!" -> `[Nút: Chụp CCCD]`.
4.  **In-Progress / Tracking (Trạng thái Đang xử lý):**
    *   *Sử dụng khi:* Khách đang chờ hệ thống xử lý (Giao hàng, Kỹ thuật viên đến).
    *   *Ví dụ:* "Đơn hàng SIM số đẹp của bạn đang được giao. Xem hành trình." (Có thanh Progress Bar).
5.  **Success / Rewarding (Trạng thái Thành công):**
    *   *Sử dụng khi:* Chúc mừng khi hoàn thành tác vụ. Tạo hiệu ứng thị giác tích cực (Delightful UX).
    *   *Ví dụ:* Hiện Icon tích xanh lớn - "Bạn đã thanh toán đủ cước tháng này. Cảm ơn bạn!".

### C. Template hiển thị (Card-based UI)
*   **Cấu trúc:** Sử dụng các khối thẻ (Cards) với viền bo tròn, bóng đổ nhẹ tạo cảm giác phân lớp (elevation).
*   **Layout:** Linh hoạt các kích thước thẻ (1x1, 2x1, 2x2) để ghép nối vừa vặn.
*   **Phân bổ thông tin trên thẻ (Cho Normal State):**
    *   *Tiêu đề phụ:* Tên loại thông tin (Tài khoản chính, Lưu lượng Data).
    *   *Thông số chính:* Font size lớn nhất, in đậm (3.500đ, 2.048 MB) để "quét" nhanh bằng mắt.
    *   *Trạng thái/Chỉ báo:* Các mũi tên lên/xuống màu Đỏ/Xanh so sánh với kỳ trước.
    *   *Call-to-action:* Rút ngắn hành trình bằng nút bấm cực ngắn (như dấu `+` để nạp ngay).

### D. Tiêu chuẩn Quản trị & Tối ưu Widget (Chống Widget Overload)

Để tránh tình trạng màn hình Home biến thành một "nồi lẩu thập cẩm" gây quá tải nhận thức, hệ thống cần chủ động điều phối sự xuất hiện của các Widget thông qua 3 chiến lược:

1.  **Thuật toán Sắp xếp Động (State-Driven Sorting):**
    *   Tận dụng chính 5 Lifecycle States để làm "trọng số" sắp xếp.
    *   *Ưu tiên 1 (Top Hero):* Widget ở State 3 (Cảnh báo khẩn) hoặc State 4 (Đang xử lý) tự động trồi lên trên cùng.
    *   *Ưu tiên 2 (Middle):* Widget ở State 2 (Bình thường) nằm ở khu vực giữa.
    *   *Ưu tiên 3 (Bottom/Hidden):* Widget ở State 1 (Rỗng) bị đẩy xuống cuối hoặc thu nhỏ lại.
2.  **Giới hạn Không gian (Bento Grid) và Tự động Gom nhóm:**
    *   *Giới hạn Slot:* Màn hình Home chỉ có số lượng lưới (Grid) cố định. Khách hàng chỉ được ghim một lượng tối đa Widget (VD: tối đa 6 slots). Muốn thêm mới phải bỏ bớt cái cũ.
    *   *Gom nhóm ngang (Carousel):* Các Widget cùng nhóm chức năng (như 5 thiết bị SmartHome) không được xếp dọc, mà phải gom chung vào 1 hàng vuốt ngang.
3.  **Ẩn/Hiện theo Ngữ cảnh (Contextual Visibility):**
    *   Widget chỉ hiển thị khi có giá trị về mặt thời gian và không gian.
    *   *Ví dụ:* Widget "Chuyến bay sắp tới" chỉ xuất hiện trước 24h cất cánh, và tự động biến mất sau khi hạ cánh, giúp tự dọn dẹp rác hiển thị trên màn hình.

---

## 2. Nhóm FEEDS: Dòng thời gian Cá nhân hóa (Emi Speak Out)

Nếu Widget là nơi KH "nhìn vào bản thân", thì Feeds là nơi **Emi chủ động "trò chuyện" và mang thế giới bên ngoài đến cho KH**. 

Quan điểm cốt lõi: Emi là **MỘT thực thể duy nhất** (Trợ lý số gia đình). Chúng ta không nhân bản Emi thành nhiều tính cách (Persona) khác nhau để tránh làm loãng thương hiệu. Thay vào đó, chúng ta phân loại **Tuyến nội dung (Content Pillars)** mà Emi truyền tải, kết hợp với bộ lọc **Ngữ cảnh (Context-Aware)** để phân phối tin tức.

### A. 4 Tuyến nội dung (Content Pillars) trên Feeds
Emi sẽ trò chuyện với khách hàng xoay quanh 4 chủ đề chính:

1.  **Tin tức Dịch vụ & Hệ thống (Service Updates):** 
    *   *Mục đích:* Thể hiện sự minh bạch, thấu cảm. 
    *   *Nội dung:* Lịch bảo trì trạm phát sóng, thông báo đứt cáp quang biển, nâng cấp hệ thống thanh toán. 
    *   *Trigger:* Chỉ xuất hiện khi hệ thống Backend phát hiện khu vực sống/dịch vụ của User bị ảnh hưởng.
2.  **Gợi ý Tiêu dùng Thông minh (Smart Recommendations):** 
    *   *Mục đích:* Bán chéo/Up-sell dịch vụ cốt lõi một cách tinh tế (Soft-selling).
    *   *Nội dung:* Đề xuất gói cước, mua thêm Data, giới thiệu SIM mới.
    *   *Trigger:* Dựa trên Location (VD: Khách đến sân bay -> Gợi ý Roaming) hoặc Hành vi (VD: Cạn Data -> Gợi ý gói bổ sung).
3.  **Khám phá Tiện ích (Feature Discovery):** 
    *   *Mục đích:* Educate người dùng, tăng cường sử dụng các dịch vụ Non-Telco.
    *   *Nội dung:* Giới thiệu Mua Vietlott, Đóng học phí, Đi chợ online.
    *   *Trigger:* Dựa trên mốc thời gian hoặc thói quen. (VD: Chiều Thứ 3 vắng vẻ -> Gợi ý mua 1 vé Vietlott lấy hên).
4.  **Giải trí & Cộng đồng (Entertainment & Lifestyle):** 
    *   *Mục đích:* Giữ chân người dùng (Retention), tạo cảm hứng.
    *   *Nội dung:* Phim đang hot trên MyTV, Sự kiện âm nhạc của VNPT, Mẹo vặt công nghệ.
    *   *Trigger:* Tối Thứ 6 hoặc Cuối tuần để kích thích thư giãn.

### B. Luật phân phối Feeds & Chống Spam (Mix-ratio Algorithm)

Để Feeds không biến thành "bãi rác quảng cáo", hệ thống không cho phép hiển thị bài viết vô tội vạ mà phải tuân theo thuật toán:

*   **Nguyên tắc tỷ lệ (Mix-ratio 3-1-1):** Trong một phiên lướt (scroll) gồm 5 bài viết liên tiếp trên Feeds, hệ thống chỉ cho phép xuất hiện tối đa: **1 Bài Bán hàng** (Tuyến 2) + **1 Bài Khám phá** (Tuyến 3) + **3 Bài Hữu ích/Giải trí** (Tuyến 1 và Tuyến 4). Sự xen kẽ này giữ cho trải nghiệm người dùng luôn tự nhiên.
*   **Tần suất (Frequency Capping):** Mỗi User chỉ nhận tối đa 2 Post mới mỗi ngày.
*   **Quyền Lên tiếng (Priority):** Tuyến 1 (Tin tức hệ thống đứt mạng/bảo trì) luôn có đặc quyền "đâm ngang" và đẩy lên đầu Feeds bất kỳ lúc nào để xoa dịu khách hàng.
*   **Tiến hóa theo User State:** Khách Ẩn danh/Vãng lai (State 0, 4) sẽ thấy Feeds đại chúng (Tuyến 3, 4). Khách định danh chuẩn (State 1) sẽ thấy Feeds cá nhân hóa cao độ (Tuyến 1, 2).
*   **Giới hạn hiển thị (Finite Feed - Bản tin trong ngày):** Tuyệt đối KHÔNG sử dụng thiết kế "Cuộn vô tận" (Infinity Scroll) cho Feeds trên màn hình Home. Feeds tại đây hoạt động như một bản tin tóm tắt, chỉ hiển thị tối đa **5 bài viết (posts)** quan trọng nhất. Dưới bài thứ 5 là nút bấm `[Khám phá thêm]` để dẫn khách hàng sang một Tab riêng (tại Tab riêng này mới áp dụng Infinity Scroll). Cấu trúc này giúp tránh gây loãng mục tiêu chính và tối ưu Performance cho Home screen.

### C. Template hiển thị (Timeline/Newsfeed UI)
*   **Cấu trúc:** Tương tự Newsfeed của Facebook/Zalo, trải dọc từ trên xuống.
*   **Thành phần cấu tạo 1 Post:**
    *   **Header:** Avatar của Emi (duy nhất 1 nhận diện) + Tên "Emi" + Thời gian đăng. Góc phải có menu "..." để KH phản hồi (Ẩn tin này, Không quan tâm...).
    *   **Body (Copywriting):** Giọng văn thân thiện, xưng hô cá nhân hóa, tuyệt đối không dùng thuật ngữ kỹ thuật (No-jargon).
    *   **Rich Media:** Ảnh banner đơn, hoặc Carousel vuốt ngang (danh sách gói cước, danh sách phim). Thiết kế thẻ sản phẩm bên trong cần kèm Social Proof (lượt mua, rating) hoặc thẻ tag.
    *   **Footer (Action Area):** Các nút CTA dạng text hoặc button nhẹ nhàng (Xem chi tiết, Đặt vé ngay).

---

## Tổng kết
Sự phân tách này là một quy hoạch UI/UX rất hiện đại: **Widget giải quyết "Nhu cầu hiện tại" (Needs)** một cách nhanh gọn, trong khi **Feeds khơi gợi "Mong muốn tiềm năng" (Wants)** một cách tinh tế. Hai luồng thông tin này chạy song song sẽ giúp app MyVNPT vừa duy trì được vai trò tiện ích cốt lõi, vừa mở rộng được không gian thương mại và gắn kết cộng đồng.

---

## 3. Định hướng Thiết kế Thị giác (UI/Visual Guidelines)

Để đảm bảo thiết kế giao diện mang đậm định vị **Premium (Cao cấp)** và **Human-centric (Trợ lý cá nhân)**, hai cấu phần Widget và Feeds cần tuân thủ triết lý: *Widget là "Less is More" (Tối giản) – Feeds là "Rich & Engaging" (Sống động).*

### A. Hình khối và Hệ thống lưới (Grid & Shape)
Nhằm tạo ra sự phân tách bằng thị giác giữa "Khu vực Quản lý" (Widget) và "Khu vực Tin tức" (Feeds):
*   **Widget UI (Bento Box):** Sử dụng thiết kế lưới hộp (Bento Grid). Các Widget ghép lại thành một khối vuông vức. Sử dụng góc bo tròn lớn (24px - 32px) để tạo cảm giác thân thiện. Dùng bóng đổ nhạt (Soft shadow) để nhấc nổi Widget.
*   **Feeds UI (Social Cards):** Mỗi Post là một thẻ độc lập (Card) với khoảng trắng (Negative space) rộng rãi. Bắt buộc có Header cố định (`Avatar Emi + Tên + Thời gian`) làm điểm neo thị giác.

### B. Ngôn ngữ Màu sắc & Kiểu chữ (Typography & Colors)
*   **Quiet UI (Giao diện Tĩnh lặng) cho trạng thái Bình thường:** Nền trắng hoặc xám nhạt, màu Xanh VNPT chỉ dùng làm điểm nhấn (Accent). Con số (Data, Tiền) trong Widget phải cực to (Display font) và bôi đậm để quét mắt nhanh trong 0.5s.
*   **Shout-out (Giao diện Cảnh báo) cho trạng thái Alert:** Không chỉ bôi đỏ text, mà chuyển *toàn bộ màu nền* của khối Widget sang tone màu cảnh báo (Đỏ/Cam nhạt) để tạo sức nặng thị giác lập tức.
*   **Rich Media trên Feeds:** Không để bài viết toàn chữ. Ưu tiên hình thức **Carousel vuốt ngang** cho các bài gợi ý gói cước, thiết kế như những "chiếc vé" (Ticket) hấp dẫn thay vì bảng biểu khô khan.

### C. Tương tác và Chuyển động (Micro-Interactions)
Tạo cảm giác Emi là một thực thể "sống":
*   **Animation cho Widget:** Khi Widget có cảnh báo khẩn, áp dụng hiệu ứng **Pulse (Nhịp đập)** nhẹ nhàng để thu hút mắt. Khi nạp tiền/hoàn thành tác vụ (Success State), xuất hiện pháo giấy mini (Confetti) bên trong thẻ.
*   **Loading & Truncation cho Feeds:** Sử dụng bộ khung mờ (Skeleton Loading) hình bài viết thay cho vòng tròn xoay (Spinner) để tối ưu cảm giác chờ đợi. Các đoạn Text giới hạn tối đa 3 dòng, muốn đọc phải ấn "Xem thêm" (Truncation) để Feeds luôn gọn gàng.

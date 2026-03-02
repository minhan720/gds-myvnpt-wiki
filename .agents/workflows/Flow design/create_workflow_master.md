---
description: Pipeline Xuyên Mạch - Kích hoạt tự động chuỗi Super UX (3 Phases + HITL)
---

# Super UX Master Workflow

**Mục tiêu:** Luồng gọi lệnh chóp bu (Master Command) dùng để tự động hóa phần Mở Session, nhưng vẫn giữ chặt 3 chốt chặn phê duyệt của Con người (HITL - Human in the Loop).

1. **Khởi Trình:** Yêu cầu User cung cấp thông tin bài toán/thị trường cần làm thiết kế UX.
// turbo-all
2. **Kích hoạt Phase 1 (Khảo sát gốc rễ):**
   - Đóng vai `PG-UX Researcher`.
   - Chạy workflow tại `/.agents/workflows/Flow design/create_workflow_phase1_moments.md`.
   - Dừng lại ở Cuối Phase 1 và thông báo: `[HITL 1] Chờ Boss duyệt tệp ux_research_insight.md`. (Chỉ đi tiếp khi có lệnh Approve).
3. **Kích hoạt Phase 2 (Định hình Giải pháp):**
   - Đóng vai `Empathy Strategist`.
   - Đọc Insight mồi, chạy workflow tại `/.agents/workflows/Flow design/create_workflow_phase2_strategy.md`.
   - Dừng lại ở Cuối Phase 2 và thông báo: `[HITL 2] Chờ Boss duyệt tệp empathy_strategy_blueprint.md`. (Chỉ đi tiếp khi có lệnh Approve).
4. **Kích hoạt Phase 3 (Thiết kế luồng & UI Specs):**
   - Đóng vai `UX Designer & Writer`.
   - Đọc Blueprint, chạy workflow tại `/.agents/workflows/Flow design/create_workflow_phase3_spec_design.md`.
   - Báo cáo kết thúc dự án: `[HITL 3] Trình Boss duyệt Specs & UX Flows và Feedback`.

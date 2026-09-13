# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Lê Hoàng Đạt 
> **Mã Sinh Viên / Mã Học viên:** 2A202602583
> **Chủ đề Lựa chọn:** Trợ lý Dịch vụ Khách hàng VinBus  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Nhiều yêu cầu cần xử lý qua nhiều bước, ví dụ: xác định nhu cầu → tìm tuyến → kiểm tra điểm lên/xuống → tra lịch trình → đưa hướng dẫn. |
| **2. Tool Interaction** | 5 / 5 | Agent có thể cần tương tác với nhiều tool/API để tra cứu tuyến, lịch xe, điểm dừng, giá vé, tình trạng dịch vụ… |
| **3. Dynamic Decision** | 5 / 5 | Agent phải tự quyết định có cần dùng tool không, dùng tool nào, và dùng tiếp tool nào dựa trên kết quả trước đó. Ví dụ nếu khách chỉ đưa tên điểm đến, agent có thể phải tìm tuyến phù hợp rồi mới kiểm tra lịch chạy. |
| **4. Long Horizon Goal** | 3 / 5 | Một số task có thể kéo dài qua nhiều bước, nhưng phần lớn vấn đề hỗ trợ khách hàng VinBus vẫn được giải quyết trong một phiên tương đối ngắn. Agent thường không phải theo đuổi mục tiêu kéo dài hàng giờ/ngày như các agent đặt vé, quản lý chuyến đi hay xử lý khiếu nại nhiều giai đoạn. |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin cơ bản của tuyến xe bus E03",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "route_query",
    "arguments": {
      "route_id": "E03"
    },
    "observation": {
      "status": "SUCCESS",
      "route_id": "E03",
      "data": {
        "route_name": "E03",
        "route_type": "VinBus",
        "origin": "Khu đô thị Vinhomes Ocean Park",
        "destination": "Bến xe Mỹ Đình",
        "operating_hours": "05:00 - 21:30",
        "frequency": "15 - 20 phút/chuyến",
        "stops": [
          "Vinhomes Ocean Park",
          "Cầu Chương Dương",
          "Hồ Hoàn Kiếm",
          "Cầu Giấy",
          "Bến xe Mỹ Đình"
        ],
        "status": "Đang hoạt động"
      }
    },
    "latency_ms": 1774.9
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin cơ bản của tuyến xe bus E03",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả tra cứu tuyến E03: E03. Lộ trình: Khu đô thị Vinhomes Ocean Park → Bến xe Mỹ Đình. Loại tuyến: VinBus. Giờ hoạt động: 05:00 - 21:30. Tần suất: 15 - 20 phút/chuyến. Điểm dừng: Vinhomes Ocean Park, Cầu Chương Dương, Hồ Hoàn Kiếm, Cầu Giấy, Bến xe Mỹ Đình. Trạng thái: Đang hoạt động.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Tôi muốn đặt lịch đến điểm hỗ trợ khách hàng VinBus để làm lại thẻ tháng vào lúc 14:00 ngày mai. Bạn có thể đặt lịch giúp tôi không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Để có thể hỗ trợ bạn đặt lịch hẹn làm lại thẻ tháng VinBus, tôi cần thêm một số thông tin chi tiết sau. Bạn vui lòng cung cấp giúp tôi nhé:\n\n1. **Họ và tên** của bạn.\n2. **Số điện thoại** liên hệ.\n3. **Ngày hẹn cụ thể** (do tôi không rõ ngày hôm nay là ngày nào để tính ngày mai, bạn vui lòng cho biết ngày cụ thể theo định dạng Ngày/Tháng/Năm).\n4. **Điểm hỗ trợ khách hàng VinBus** mà bạn muốn đến.\n\nSau khi nhận đủ thông tin, tôi sẽ tiến hành đặt lịch ngay cho bạn!",
    "latency_ms": 3711.24
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:**  lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!

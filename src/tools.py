"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
    "name": "route_query",
    "description": "Tra cứu thông tin tuyến VinBus dựa trên tuyến, điểm đi hoặc điểm đến.",
    "parameters": {
        "type": "object",
        "properties": {
            "route_id": {
                "type": "string",
                "description": "Mã tuyến VinBus cần tra cứu nếu khách hàng biết mã tuyến (ví dụ: 'E03')."
            },
            "origin": {
                "type": "string",
                "description": "Điểm xuất phát của khách hàng."
            },
            "destination": {
                "type": "string",
                "description": "Điểm đến của khách hàng."
            }
        },
        "required": []
    }
    },
    
    {
    "name": "schedule_appointment",
    "description": "Đặt lịch đến điểm hỗ trợ khách hàng Vinbus để làm lại vé tháng.",
    "parameters": {
        "type": "object",
        "properties": {
            "appointment_date": {
                "type": "string",
                "description": "Ngày khách hàng muốn đến làm lại vé, định dạng YYYY-MM-DD."
            },
            "appointment_time": {
                "type": "string",
                "description": "Thời gian khách hàng muốn đến, định dạng HH:MM."
            },
            "customer_name": {
                "type": "string",
                "description": "Họ và tên của khách hàng."
            },
            "phone_number": {
                "type": "string",
                "description": "Số điện thoại liên hệ của khách hàng."
            },
            "support_location": {
                "type": "string",
                "description": "Điểm hỗ trợ khách hàng Vinbus mà khách hàng muốn đến."
            }
        },
        "required": [
            "appointment_date",
            "appointment_time",
            "customer_name",
            "phone_number",
            "support_location"
        ]
    }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "E01": {
        "route_name": "E01",
        "route_type": "VinBus",
        "origin": "Bến xe Mỹ Đình",
        "destination": "Hào Nam",
        "operating_hours": "05:00 - 21:00",
        "frequency": "15 - 20 phút/chuyến",
        "stops": [
            "Bến xe Mỹ Đình",
            "Đại học Quốc gia Hà Nội",
            "Cầu Giấy",
            "Kim Mã",
            "Hào Nam"
        ],
        "status": "Đang hoạt động"
    },

    "E02": {
        "route_name": "E02",
        "route_type": "VinBus",
        "origin": "Khu đô thị Vinhomes Ocean Park",
        "destination": "Hào Nam",
        "operating_hours": "05:00 - 22:00",
        "frequency": "15 - 20 phút/chuyến",
        "stops": [
            "Vinhomes Ocean Park",
            "Cầu Chương Dương",
            "Long Biên",
            "Tràng Tiền",
            "Hào Nam"
        ],
        "status": "Đang hoạt động"
    },

    "E03": {
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
    },

    "E05": {
        "route_name": "E05",
        "route_type": "VinBus",
        "origin": "Long Biên",
        "destination": "Khu đô thị Smart City",
        "operating_hours": "05:30 - 21:30",
        "frequency": "15 - 20 phút/chuyến",
        "stops": [
            "Long Biên",
            "Hồ Hoàn Kiếm",
            "Kim Mã",
            "Nhổn",
            "Smart City"
        ],
        "status": "Đang hoạt động"
    },

    "E08": {
        "route_name": "E08",
        "route_type": "VinBus",
        "origin": "Bến xe Mỹ Đình",
        "destination": "Khu đô thị Times City",
        "operating_hours": "05:00 - 22:00",
        "frequency": "15 - 20 phút/chuyến",
        "stops": [
            "Bến xe Mỹ Đình",
            "Cầu Giấy",
            "Kim Mã",
            "Hồ Hoàn Kiếm",
            "Times City"
        ],
        "status": "Đang hoạt động"
    }
}

def execute_route_query(route_id: str) -> str:
    """Thực thi tra cứu thông tin tuyến VinBus theo mã tuyến"""
    route = MOCK_DATABASE.get(route_id.strip().upper())

    if route:
        return json.dumps({
            "status": "SUCCESS",
            "route_id": route_id.strip().upper(),
            "data": route
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy thông tin tuyến VinBus có mã '{route_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(
    appointment_date: str,
    appointment_time: str,
    customer_name: str,
    phone_number: str,
    support_location: str
) -> str:
    """Thực thi đặt lịch đến điểm hỗ trợ khách hàng VinBus để làm lại vé tháng"""

    booking_id = f"VB-{appointment_date.replace('-', '')}-{phone_number[-4:]}"

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": booking_id,
        "customer_name": customer_name,
        "phone_number": phone_number,
        "appointment_date": appointment_date,
        "appointment_time": appointment_time,
        "support_location": support_location,
        "service": "Làm lại vé tháng",
        "message": (
            f"Đặt lịch thành công cho {customer_name} "
            f"vào lúc {appointment_time} ngày {appointment_date} "
            f"tại {support_location} để làm lại vé tháng."
        )
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "route_query": execute_route_query,
    "schedule_appointment": execute_schedule_appointment
}


# TODO 2.1: Hoàn thiện hàm điều tuyến dispatch_tool_call
def dispatch_tool_call(
    tool_name: str,
    arguments: Dict[str, Any]
) -> str:
    """Hàm trung chuyển thực thi tool"""

    if tool_name == "route_query":
        try:
            return execute_route_query(**arguments)

        except TypeError as e:
            return json.dumps({
                "status": "INVALID_ARGUMENTS",
                "error": str(e)
            }, ensure_ascii=False)

        except Exception as e:
            return json.dumps({
                "status": "EXECUTION_ERROR",
                "error": str(e)
            }, ensure_ascii=False)

    elif tool_name == "schedule_appointment":
        try:
            return execute_schedule_appointment(**arguments)

        except TypeError as e:
            return json.dumps({
                "status": "INVALID_ARGUMENTS",
                "error": str(e)
            }, ensure_ascii=False)

        except Exception as e:
            return json.dumps({
                "status": "EXECUTION_ERROR",
                "error": str(e)
            }, ensure_ascii=False)

    else:
        return json.dumps({
            "status": "UNKNOWN_TOOL",
            "error": f"Tool '{tool_name}' không tồn tại!"
        }, ensure_ascii=False)
# tingee-sdk (Python)

> SDK chính thức tích hợp **Tingee Open API** cho Python

Python ≥ 3.8, không phụ thuộc thư viện ngoài.

---

## Cài đặt

```bash
pip install tingee-sdk
```

---

## Bắt đầu nhanh

```python
import os
from tingee_sdk import TingeeClient, is_success_response

client = TingeeClient(
    secret_key=os.environ["TINGEE_SECRET_KEY"],
    client_id=os.environ["TINGEE_CLIENT_ID"],
    environment="uat",  # hoặc "production" (mặc định)
)

result = client.bank.get_banks()
if is_success_response(result):
    print(result["data"])

result = client.bank.generate_viet_qr({
    "bankName": "OCB",
    "accountNumber": "0123456789",
    "amount": 100000,
    "content": "Thanh toan don hang",
})
```

- Method được nhóm theo path: `/v1/bank/create-va` → `client.bank.create_va(body)`, `/v1/deep-link/generate` → `client.deep_link.generate(body)`.
- Body và query truyền dạng `dict`, tên field giữ nguyên như API (camelCase). Kiểu DTO (TypedDict) nằm trong `tingee_sdk.models`.
- SDK tự ký request (`x-signature`, `x-request-timestamp`, `x-client-id`).

> **Lưu ý:** SDK trả về `dict` có `code` và `message`. Kiểm tra `code == "00"` hoặc `is_success_response(result)` để xác định thành công — SDK **không tự raise** khi `code != "00"`. Lỗi HTTP (non-2xx), lỗi mạng và timeout raise `TingeeHttpError`.

---

## Xác thực Webhook

```python
# Flask
from flask import Flask, request

app = Flask(__name__)

@app.post("/webhook/tingee")
def tingee_webhook():
    result = client.verify_webhook_signature(
        request.headers.get("x-signature"),
        request.headers.get("x-request-timestamp"),
        request.get_data(),  # raw body
    )
    if result["code"] != "00":
        return {"error": result["message"]}, 401

    body = request.get_json()
    # Xử lý giao dịch...
    return {"received": True}
```

Hoặc dùng hàm `verify_webhook_signature(secret_token, signature, timestamp, body)` với secret token riêng.

---

## Xác thực URL webhook

Khi lưu URL webhook trên Tingee, hệ thống gửi một request xác thực vào URL đó:

```json
{ "event": "url-validation", "plainToken": "<chuỗi ngẫu nhiên>", "timestamp": 1730000000000 }
```

Endpoint phải trả về HTTP 200 với `{ "plainToken": "...", "encryptedToken": "..." }`, trong đó `encryptedToken = HMAC-SHA256(secretToken, plainToken)` dạng hex. `secretToken` là secret của **API Key loại Xác thực webhook** đang bật (tạo trong mục API Credentials).

SDK làm sẵn bước này: hàm trả về body cần phản hồi, hoặc `None` nếu không phải request xác thực. Gọi **trước** khi verify chữ ký, vì body xác thực không có các trường giao dịch.

```python
from tingee_sdk import create_url_validation_response

@app.post("/webhook/tingee")
def tingee_webhook():
    validation = create_url_validation_response(os.environ["TINGEE_WEBHOOK_SECRET"], request.get_data())
    if validation is not None:
        return validation

    # Verify chữ ký & xử lý giao dịch như bình thường...
```

Nếu dùng chung khóa với client: `client.create_url_validation_response(request.get_data())`.

---

## Bank Constants

```python
from tingee_sdk import BankNameEnum, get_bank_code, get_bank_short_name, get_bank_bin

get_bank_code("970436")                 # BankNameEnum.VCB
get_bank_short_name("970436")           # 'Vietcombank'
get_bank_bin(BankNameEnum.VCB)          # '970436'
```

---

## Liên hệ & Hỗ trợ

📧 **Email:** [developer@heno.vn](mailto:developer@heno.vn)
💬 **Telegram:** [@tingeesupport](https://t.me/tingeesupport)
🌐 **Website:** [tingee.vn](https://tingee.vn)

---

## Xem thêm

- [CHANGELOG](./CHANGELOG.md)
- [Tài liệu Tingee Open API](https://open-api.tingee.vn)
- [Tài liệu Tingee Developer](https://developers.tingee.vn)
- [Trang chủ Tingee](https://tingee.vn)

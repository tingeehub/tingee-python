# Changelog — tingee-sdk (Python)

## [0.4.0] — 2026-11-09

### Added
- Method mới: `device.clear_screen`, `device.get_features`, `device.notify_order`
- `deepLink.generate`: thêm field `platform` (1 = Android, 2 = iOS)

### Changed (breaking)
- Field bắt buộc của DTO request được tính lại theo validate thực tế của server. Các field trước đây bị đánh dấu bắt buộc nhầm nay là tuỳ chọn, ví dụ `appType`, `minAmount`, `maxAmount` của `createVa`; `merchantId`, `dataAccess`, `transactionType` của `getVaPaging`; `bankName` của `confirmVa`; `password`, `appType` của `merchant.create`
- Chú thích `# optional` trong `tingee_sdk.models` cập nhật theo danh sách mới; TypedDict vẫn `total=False` nên code cũ không bị ảnh hưởng

## [0.3.1] — 2026-11-06

### Added
- Gửi header `User-Agent: tingee-sdk-python/<version> (python/<version>; <platform>)` trong mọi request
- Phiên bản đầu tiên của SDK Python, sinh tự động từ OpenAPI spec như các SDK khác
- `TingeeClient` tự ký request, method nhóm theo path (`client.bank.create_va(...)`), DTO TypedDict trong `tingee_sdk.models`
- `verify_webhook_signature`, `create_url_validation_response`, `generate_signature`, `format_timestamp`
- Bank constants: `BankNameEnum`, `BankBinEnum`, `get_bank_code`, `get_bank_short_name`, `get_bank_bin`

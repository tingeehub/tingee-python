# Auto-generated from openapi/sdk.json
# DO NOT EDIT MANUALLY
# flake8: noqa

from __future__ import annotations

from typing import Any, Dict, Optional

from . import models
from .http import TingeeHttpClient
from .response import TingeeApiResponse


class BankApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def generate_viet_qr(self, body: models.OpenApiGenerateVietQRInputDto) -> TingeeApiResponse:
        """POST /v1/bank/generate-viet-qr

        Response data: GenerateVietQROuputDto
        """
        return self._http.request('post', '/v1/bank/generate-viet-qr', body=body)

    def generate_dynamic_qr(self, body: models.GenerateDynamicQRInputDto) -> TingeeApiResponse:
        """POST /v1/bank/generate-dynamic-qr

        Response data: GenerateDynamicQROuputDto
        """
        return self._http.request('post', '/v1/bank/generate-dynamic-qr', body=body)

    def delete_dynamic_qr(self, body: models.OpenApiDeleteDynamicQRInputDto) -> TingeeApiResponse:
        """POST /v1/bank/delete-dynamic-qr

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/bank/delete-dynamic-qr', body=body)

    def get_status_dynamic_qr(self, body: models.OpenApiGetStatusDynamicQRInputDto) -> TingeeApiResponse:
        """POST /v1/bank/get-status-dynamic-qr

        Response data: OpenApiGetStatusDynamicQROutputDto
        """
        return self._http.request('post', '/v1/bank/get-status-dynamic-qr', body=body)

    def get_banks(self) -> TingeeApiResponse:
        """GET /v1/bank/get-banks

        Response data: List[Bank]
        """
        return self._http.request('get', '/v1/bank/get-banks')

    def get_va_paging(self, body: models.OpenApiGetVAPagedInputDto) -> TingeeApiResponse:
        """POST /v1/bank/get-va-paging

        Response data: PagedResultDto[OpenApiGetVAPagedOuputDto]
        """
        return self._http.request('post', '/v1/bank/get-va-paging', body=body)

    def get_account_number_info_by_qr_code(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """POST /v1/bank/get-account-number-info-by-qr-code

        Query params:
            qrCode (str)

        Response data: PagedResultDto[OpenApiGenerateVietQROuputDto]
        """
        return self._http.request('post', '/v1/bank/get-account-number-info-by-qr-code', query=query)

    def create_va(self, body: models.OpenApiCreateVAInpuDto) -> TingeeApiResponse:
        """POST /v1/bank/create-va

        Response data: BankCreateVAOuputDto
        """
        return self._http.request('post', '/v1/bank/create-va', body=body)

    def create_va_advanced(self, body: models.OpenApiCreateVAInpuDto) -> TingeeApiResponse:
        """POST /v1/bank/create-va-advanced

        Response data: BankCreateVAOuputDto
        """
        return self._http.request('post', '/v1/bank/create-va-advanced', body=body)

    def confirm_va(self, body: models.OpenApiBankConfirmVAInputDto) -> TingeeApiResponse:
        """POST /v1/bank/confirm-va

        Response data: OpenApiConfirmVAOuputDto
        """
        return self._http.request('post', '/v1/bank/confirm-va', body=body)

    def delete_va(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """POST /v1/bank/delete-va

        Query params:
            bankBin (str, optional)
            bankName (BankNameEnum, optional)
            vaAccountNumber (str)
            merchantId (float, optional)

        Response data: BankDeleteVAOutputDto
        """
        return self._http.request('post', '/v1/bank/delete-va', query=query)

    def confirm_delete_va(self, body: models.OpenApiBankConfirmVAInputDto) -> TingeeApiResponse:
        """POST /v1/bank/confirm-delete-va

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/bank/confirm-delete-va', body=body)

    def register_notify(self, body: models.OpenApiRegisterNotifyDto) -> TingeeApiResponse:
        """POST /v1/bank/register-notify

        Response data: BankDeleteVAOutputDto
        """
        return self._http.request('post', '/v1/bank/register-notify', body=body)

    def webhook_notification(self, body: models.UpdateWebhookNotificationDto) -> TingeeApiResponse:
        """POST /v1/bank/webhook-notification

        Response data: Boolean
        """
        return self._http.request('post', '/v1/bank/webhook-notification', body=body)

    def create_bank_link_session(self, body: models.CreateBankLinkSessionInputDto) -> TingeeApiResponse:
        """POST /v1/bank/create-bank-link-session

        Response data: String
        """
        return self._http.request('post', '/v1/bank/create-bank-link-session', body=body)

    def confirm_register_notify(self, body: models.OpenApiBankConfirmVAInputDto) -> TingeeApiResponse:
        """POST /v1/bank/confirm-register-notify

        Response data: BankDeleteVAOutputDto
        """
        return self._http.request('post', '/v1/bank/confirm-register-notify', body=body)


class DeviceApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def read_security_code(self, body: models.OpenApiReadSecurityCodeDto) -> TingeeApiResponse:
        """POST /v1/device/read-security-code

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/read-security-code', body=body)

    def add_device_to_shop(self, body: models.OpenApiAddDeviceToShop) -> TingeeApiResponse:
        """POST /v1/device/add-device-to-shop

        Response data: List[SendNotifyTingeeBoxDto]
        """
        return self._http.request('post', '/v1/device/add-device-to-shop', body=body)

    def update_shop_device_link_status(self, body: models.OpenApiUpdateShopDeviceLinkDto) -> TingeeApiResponse:
        """POST /v1/device/update-shop-device-link-status

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/update-shop-device-link-status', body=body)

    def read_amount_link_to_merchant(self, body: models.OpenApiReadAmountDto) -> TingeeApiResponse:
        """POST /v1/device/read-amount-link-to-merchant

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/read-amount-link-to-merchant', body=body)

    def show_qr_code(self, body: models.OpenApiShowQRCodeDto) -> TingeeApiResponse:
        """POST /v1/device/show-qr-code

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/show-qr-code', body=body)

    def show_dynamic_qr_code(self, body: models.OpenApiShowQRCodeDto) -> TingeeApiResponse:
        """POST /v1/device/show-dynamic-qr-code

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/show-dynamic-qr-code', body=body)

    def show_static_qr_code(self, body: models.OpenApiShowQRCodeDto) -> TingeeApiResponse:
        """POST /v1/device/show-static-qr-code

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/show-static-qr-code', body=body)

    def clear_screen(self, body: models.OpenApiClearDeviceScreenDto) -> TingeeApiResponse:
        """POST /v1/device/clear-screen

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/clear-screen', body=body)

    def get_devices_link_to_shop_or_va(self, body: models.OpenApiGetDevicesLinkToShopOrVA) -> TingeeApiResponse:
        """POST /v1/device/get-devices-link-to-shop-or-va

        Response data: List[SendNotifyTingeeBoxDto]
        """
        return self._http.request('post', '/v1/device/get-devices-link-to-shop-or-va', body=body)

    def get_paging(self, body: models.OpenApiGetPagingDeviceInputDto) -> TingeeApiResponse:
        """POST /v1/device/get-paging

        Response data: PagedResultDto[DeviceDto]
        """
        return self._http.request('post', '/v1/device/get-paging', body=body)

    def reset(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """DELETE /v1/device/reset

        Query params:
            uuid (str)

        Response data: String
        """
        return self._http.request('delete', '/v1/device/reset', query=query)

    def generate_and_show_dynamic_qr_code(self, body: models.OpenApiGenerateAndShowDynamicQrCodeDto) -> Any:
        """POST /v1/device/generate-and-show-dynamic-qr-code

        Response data: bytes (raw response)
        """
        return self._http.request('post', '/v1/device/generate-and-show-dynamic-qr-code', body=body)

    def print_receipt(self, body: models.OpenApiPrintReceiptDto) -> TingeeApiResponse:
        """POST /v1/device/print-receipt

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/print-receipt', body=body)

    def nfc_command(self, body: models.OpenApiNfcCommandDto) -> TingeeApiResponse:
        """POST /v1/device/nfc-command

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/nfc-command', body=body)

    def notify_order(self, body: models.OpenApiDeviceNotifyOrderDto) -> TingeeApiResponse:
        """POST /v1/device/notify-order

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/notify-order', body=body)

    def get_features(self, body: models.OpenApiGetDeviceFeaturesDto) -> TingeeApiResponse:
        """POST /v1/device/get-features

        Response data: OpenApiDeviceFeaturesOutputDto
        """
        return self._http.request('post', '/v1/device/get-features', body=body)

    def reset_device(self, body: models.OpenApiResetDeviceDto) -> TingeeApiResponse:
        """POST /v1/device/reset-device

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/device/reset-device', body=body)


class ShopApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def create_or_update(self, body: models.OpenApiCreateOrUpdateShopDto) -> TingeeApiResponse:
        """POST /v1/shop/create-or-update

        Response data: OpenApiCreateOrUpdateShopOutputDto
        """
        return self._http.request('post', '/v1/shop/create-or-update', body=body)

    def get_paging(self, body: models.OpenApiGetShopPagedInputDto) -> TingeeApiResponse:
        """POST /v1/shop/get-paging

        Response data: PagedResultDto[OpenApiGetShopPagedOuputDto]
        """
        return self._http.request('post', '/v1/shop/get-paging', body=body)


class DeepLinkApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def generate(self, body: models.OpenApiDeepLinkDto) -> TingeeApiResponse:
        """POST /v1/deep-link/generate

        Response data: String
        """
        return self._http.request('post', '/v1/deep-link/generate', body=body)


class TransactionApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def get_paging(self, body: models.OpenApiTransactionPagedInputDto) -> TingeeApiResponse:
        """POST /v1/transaction/get-paging

        Response data: PagedResultDto[OpenApiTransactionPagedOuputDto]
        """
        return self._http.request('post', '/v1/transaction/get-paging', body=body)


class MerchantApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def get_paging_config(self, body: models.OpenApiMerchantBankConfigPagedInputDto) -> TingeeApiResponse:
        """POST /v1/merchant/get-paging-config

        Response data: PagedResultDto[MerchantBankConfigPagedOutputDto]
        """
        return self._http.request('post', '/v1/merchant/get-paging-config', body=body)

    def create_or_update_config(self, body: models.OpenApiBankCreateOrUpdateConfigDto) -> TingeeApiResponse:
        """POST /v1/merchant/create-or-update-config

        Response data: float
        """
        return self._http.request('post', '/v1/merchant/create-or-update-config', body=body)

    def delete_config(self, body: models.OpenApiDeleteConfigDto) -> TingeeApiResponse:
        """POST /v1/merchant/delete-config

        Response data: float
        """
        return self._http.request('post', '/v1/merchant/delete-config', body=body)

    def config_account_business(self, body: models.OpenApiConfigAccountBusinessDto) -> TingeeApiResponse:
        """POST /v1/merchant/config-account-business

        Response data: OpenApiCreateBankVAOutputDto
        """
        return self._http.request('post', '/v1/merchant/config-account-business', body=body)

    def delete_config_account_business(self, body: models.OpenApiDeleteConfigBusinessDto) -> TingeeApiResponse:
        """POST /v1/merchant/delete-config-account-business

        Response data: Union[bool, BankDeleteVAOutputDto]
        """
        return self._http.request('post', '/v1/merchant/delete-config-account-business', body=body)

    def create(self, body: models.OpenApiCreateMerchantDto) -> TingeeApiResponse:
        """POST /v1/merchant/create

        Response data: OpenApiMerchantIdDto
        """
        return self._http.request('post', '/v1/merchant/create', body=body)

    def get_paging(self, body: models.OpenApiGetPagingMerchantsDto) -> TingeeApiResponse:
        """POST /v1/merchant/get-paging

        Response data: PagedResultDto[MerchantDto]
        """
        return self._http.request('post', '/v1/merchant/get-paging', body=body)

    def delete(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """DELETE /v1/merchant/delete

        Query params:
            merchantId (float)

        Response data: EmptyDto
        """
        return self._http.request('delete', '/v1/merchant/delete', query=query)


class DirectDebitApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def register(self, body: models.OpenApiRegisterDto) -> TingeeApiResponse:
        """POST /v1/direct-debit/register

        Response data: String
        """
        return self._http.request('post', '/v1/direct-debit/register', body=body)

    def payment_bill(self, body: models.OpenApiPaymentBillDto) -> TingeeApiResponse:
        """POST /v1/direct-debit/payment-bill

        Response data: PaymentBillResponseDto
        """
        return self._http.request('post', '/v1/direct-debit/payment-bill', body=body)

    def delete_subscription(self, body: models.OpenApiDeleteSubscriptionDto) -> TingeeApiResponse:
        """DELETE /v1/direct-debit/delete-subscription

        Response data: DeleteSubscriptionOutputDto
        """
        return self._http.request('delete', '/v1/direct-debit/delete-subscription', body=body)

    def refund(self, body: models.OpenApiRefundInputDto) -> TingeeApiResponse:
        """POST /v1/direct-debit/refund

        Response data: RefundOutputDto
        """
        return self._http.request('post', '/v1/direct-debit/refund', body=body)

    def edit_confirm_payment_method(self, body: models.OpenApiEditConfirmBeforePaymentMethodDto) -> TingeeApiResponse:
        """PUT /v1/direct-debit/edit-confirm-payment-method

        Response data: String
        """
        return self._http.request('put', '/v1/direct-debit/edit-confirm-payment-method', body=body)

    def get_subscription_status(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """GET /v1/direct-debit/get-subscription-status

        Query params:
            requestId (str, optional)
            subscriptionId (str)
            tokenRef (str)

        Response data: OpenApiSubscriptionStatusResponseDto
        """
        return self._http.request('get', '/v1/direct-debit/get-subscription-status', query=query)

    def get_transaction_status(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """GET /v1/direct-debit/get-transaction-status

        Query params:
            transactionId (str)
            tokenRef (str)
            subscriptionId (str)

        Response data: OpenApiPaymentTransactionStatusResponseDto
        """
        return self._http.request('get', '/v1/direct-debit/get-transaction-status', query=query)

    def get_paging_transactions(self, query: Dict[str, Any]) -> TingeeApiResponse:
        """GET /v1/direct-debit/get-paging-transactions

        Query params:
            subscriptionId (str)
            tokenRef (str)
            startTime (str, optional)
            endTime (str, optional)
            skipCount (float, optional)
            maxResultCount (float, optional)

        Response data: PagedResultDto[OpenApiPaymentTransactionsPagedOutputDto]
        """
        return self._http.request('get', '/v1/direct-debit/get-paging-transactions', query=query)


class EInvoiceApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def get_paging_account(self, body: models.GetPagingEInvoiceAccountInputDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/get-paging-account

        Response data: PagedResultDto[GetPagingEInvoiceAccountOutputDto]
        """
        return self._http.request('post', '/v1/e-invoice/get-paging-account', body=body)

    def create_or_update_account(self, body: models.CreateOrUpdateEInvoiceAccountDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/create-or-update-account

        Response data: float
        """
        return self._http.request('post', '/v1/e-invoice/create-or-update-account', body=body)

    def delete_account(self, body: models.DeleteEInvoiceAccountDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/delete-account

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/e-invoice/delete-account', body=body)

    def get_provider(self) -> TingeeApiResponse:
        """POST /v1/e-invoice/get-provider

        Response data: List[EInvoiceProviderDto]
        """
        return self._http.request('post', '/v1/e-invoice/get-provider')

    def create(self, body: models.CreateInvoiceDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/create

        Response data: DownloadInvoiceOutputDto
        """
        return self._http.request('post', '/v1/e-invoice/create', body=body)

    def create_and_issue(self, body: models.CreateInvoiceDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/create-and-issue

        Response data: TrackingResultDto
        """
        return self._http.request('post', '/v1/e-invoice/create-and-issue', body=body)

    def get_invoice_info(self, body: models.GetInvoiceInfoQueryDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/get-invoice-info

        Response data: TrackingResultDto
        """
        return self._http.request('post', '/v1/e-invoice/get-invoice-info', body=body)

    def download(self, body: models.DownloadInvoiceQueryDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/download

        Response data: DownloadInvoiceOutputDto
        """
        return self._http.request('post', '/v1/e-invoice/download', body=body)

    def invoice_templates(self, body: models.InvoiceTemplateInputDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/invoice-templates

        Response data: InvoiceTemplateOutputDto
        """
        return self._http.request('post', '/v1/e-invoice/invoice-templates', body=body)

    def send_email(self, body: models.SendInvoiceEmailDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/send-email

        Response data: EmptyDto
        """
        return self._http.request('post', '/v1/e-invoice/send-email', body=body)

    def input_connect(self, body: models.ConnectTCTRequestDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/input/connect

        Response data: String
        """
        return self._http.request('post', '/v1/e-invoice/input/connect', body=body)

    def input_disconnect(self, body: models.InputInvoiceBaseDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/input/disconnect

        Response data: String
        """
        return self._http.request('post', '/v1/e-invoice/input/disconnect', body=body)

    def input_sync(self, body: models.SyncIncomeInvoiceRequestDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/input/sync

        Response data: String
        """
        return self._http.request('post', '/v1/e-invoice/input/sync', body=body)

    def input_list(self, body: models.GetIncomeInvoicesListRequestDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/input/list

        Response data: IncomeInvoiceListOutputDto
        """
        return self._http.request('post', '/v1/e-invoice/input/list', body=body)

    def input_detail(self, body: models.GetIncomeInvoiceDetailRequestDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/input/detail

        Response data: IncomeInvoiceDetailOutputDto
        """
        return self._http.request('post', '/v1/e-invoice/input/detail', body=body)

    def input_preview_base64(self, body: models.GetIncomeInvoicePreviewBase64RequestDto) -> TingeeApiResponse:
        """POST /v1/e-invoice/input/preview-base64

        Response data: IncomeInvoicePreviewBase64OutputDto
        """
        return self._http.request('post', '/v1/e-invoice/input/preview-base64', body=body)


class PaymentGatewayApi:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http

    def create_link(self, body: models.OpenApiCreatePaymentLinkInputDto) -> TingeeApiResponse:
        """POST /v1/payment-gateway/create-link

        Response data: String
        """
        return self._http.request('post', '/v1/payment-gateway/create-link', body=body)


class GeneratedMethods:
    def __init__(self, http: TingeeHttpClient) -> None:
        self._http = http
        self.bank = BankApi(http)
        self.device = DeviceApi(http)
        self.shop = ShopApi(http)
        self.deep_link = DeepLinkApi(http)
        self.transaction = TransactionApi(http)
        self.merchant = MerchantApi(http)
        self.direct_debit = DirectDebitApi(http)
        self.e_invoice = EInvoiceApi(http)
        self.payment_gateway = PaymentGatewayApi(http)

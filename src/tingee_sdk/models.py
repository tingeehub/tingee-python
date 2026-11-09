# Auto-generated from openapi/sdk.json
# DO NOT EDIT MANUALLY
# flake8: noqa

from __future__ import annotations

from typing import Any, Dict, List, Literal, TypedDict, Union


class OpenApiOuputDto(TypedDict, total=False):
    code: str
    message: str
    data: Dict[str, Any]


class GenerateVietQROuputDto(TypedDict, total=False):
    qrCode: str
    qrCodeImage: str
    qrAccount: str
    referenceLabelCode: str


BankNameEnum = Literal['OCB', 'BIDV', 'MBB', 'ACB', 'VPB', 'PGB', 'VIB', 'STB', 'CTG', 'VCB', 'AGRIBANK', 'SHINHAN', 'COB', 'MSB', 'NEXTPAY', 'PAYOO', 'BAOKIM', 'TPB', 'HDB']


class OpenApiGenerateVietQRInputDto(TypedDict, total=False):
    bankBin: str  # optional
    bankName: BankNameEnum  # optional
    accountNumber: str
    amount: float  # optional
    content: str  # optional


class GenerateDynamicQROuputDto(TypedDict, total=False):
    qrCode: str
    qrAccount: str
    billId: str


QRCodeTypeEnum = Literal['dynamic-one-time-payment', 'dynamic-recurring-payment']


class GenerateDynamicQRInputDto(TypedDict, total=False):
    merchantId: float  # optional
    vaAccountNumber: str
    qrCodeType: QRCodeTypeEnum
    bankBin: str  # optional
    bankName: BankNameEnum  # optional
    name: str  # optional
    amount: float  # optional
    purpose: str  # optional
    expireInMinute: float  # optional
    extraInfo: str  # optional


class EmptyDto(TypedDict, total=False):
    pass


class OpenApiDeleteDynamicQRInputDto(TypedDict, total=False):
    merchantId: float  # optional
    qrAccount: str
    billId: str


class OpenApiBillInfoDto(TypedDict, total=False):
    billId: str
    qrCodeType: str
    bankBin: str
    accountNumber: str
    vaAccountNumber: str
    qrAccount: str
    amount: float
    purpose: str
    totalAmountPaid: float
    totalPaymentsCount: float
    expiredTime: str
    expireInMinute: float  # optional
    extraInfo: str  # optional
    status: str


CashFlowSourceEnum = Literal['bank-transfer', 'card', 'cash']


class OpenApiTransactionPagedOuputDto(TypedDict, total=False):
    transactionId: str
    merchantId: float
    shopId: float
    bankBin: str  # optional
    cashFlowSource: CashFlowSourceEnum  # optional
    code: str
    amount: float
    type: str  # optional
    content: str  # optional
    currency: str  # optional
    accountNumber: str
    vaAccountNumber: str  # optional
    transactionDate: str  # optional
    billId: str  # optional


class OpenApiGetStatusDynamicQROutputDto(TypedDict, total=False):
    billInfo: OpenApiBillInfoDto
    transactionInfos: List[OpenApiTransactionPagedOuputDto]


class OpenApiGetStatusDynamicQRInputDto(TypedDict, total=False):
    merchantId: float  # optional
    qrAccount: str
    billId: str


class Bank(TypedDict, total=False):
    code: BankNameEnum
    name: str
    shortName: str
    bin: str
    urlLogo: str
    termsAndConditions: Dict[str, Any]


class PagedResultDto(TypedDict, total=False):
    totalCount: int
    items: List[Any]


BankAccountTypeEnum = Literal['personal-account', 'business-account', 'business-household-account']


StatusMerchantAccountNumberEnum = Literal['inactive', 'active', 'lock']


TransactionTypeEnum = Literal['credit', 'debit']


class OpenApiGetVAPagedOuputDto(TypedDict, total=False):
    bankName: BankNameEnum
    bankBin: str  # optional
    accountType: BankAccountTypeEnum
    accountName: str  # optional
    accountNumber: str
    vaAccountNumber: str  # optional
    shopId: float
    status: StatusMerchantAccountNumberEnum
    creationTime: str  # optional
    transactionType: TransactionTypeEnum


DataAccessFilterEnum = Literal['referral-only', 'distributor-only']


class OpenApiGetVAPagedInputDto(TypedDict, total=False):
    filter: str
    sorting: str
    skipCount: float
    maxResultCount: float
    startTime: str
    endTime: str
    merchantId: float
    shopId: float
    accountType: BankAccountTypeEnum
    status: StatusMerchantAccountNumberEnum
    agentId: float
    dataAccess: DataAccessFilterEnum
    transactionType: TransactionTypeEnum
    bankBin: str
    bankName: BankNameEnum


class OpenApiGenerateVietQROuputDto(TypedDict, total=False):
    bankBin: str
    accountNumber: str
    amount: str  # optional
    purpose: str  # optional
    vaPrefix: str
    vaSuffix: str


OtpStbConfirmMethodEnum = Literal['SMSTTT', 'SmartOTP', 'mCode']


class Provider(TypedDict, total=False):
    pass


class Consumer(TypedDict, total=False):
    pass


class Merchant(TypedDict, total=False):
    pass


class AdditionalData(TypedDict, total=False):
    pass


class OneQRDto(TypedDict, total=False):
    isValid: bool
    provider: Provider
    consumer: Consumer
    merchant: Merchant
    additionalData: AdditionalData
    version: str
    initMethod: str
    category: str
    currency: str
    nation: str
    city: str
    crc: str


class BankCreateVAOuputDto(TypedDict, total=False):
    bankName: BankNameEnum
    merchantAccountNumberId: float
    shopId: float
    status: StatusMerchantAccountNumberEnum
    confirmId: str
    vaAccountNumber: str
    deepLink: str
    authorizeLink: str
    otpMethod: OtpStbConfirmMethodEnum
    qrDto: OneQRDto


AppTypeEnum = Literal['ocb-web', 'ocb-app', 'bidv-web', 'bidv-app', 'stb-web', 'stb-app', 'vcb-web', 'vcb-app', 'tingee-web', 'tingee-app', 'tingee-merchant-app', 'loa-hub', 'mini-app-mbb', 'mini-app-zalo', 'baas', 'TingeeMerchant']


LinkTypeEnum = Literal['api-exact', 'manual-exact', 'manual-include']


class OpenApiCreateVAInpuDto(TypedDict, total=False):
    name: str
    cashFlowSource: CashFlowSourceEnum
    accountType: BankAccountTypeEnum
    accountNumber: str
    accountName: str
    identity: str
    mobile: str
    masterMerchantId: float
    shopId: float
    vaPrefix: str
    vaSuffix: str
    merchantName: str
    merchantAddress: str
    serviceId: float
    isCreateNonOtp: bool
    code: str
    taxCode: str
    softposUserName: str
    softposDeveloperId: str
    softposTid: str
    softposMid: str
    authorizationCode: str
    sessionLogin: str
    isNotifyAccountNumber: bool
    appType: AppTypeEnum
    linkType: LinkTypeEnum
    vaAccountNumber: str
    acbUserId: str
    minAmount: float
    maxAmount: float
    isAbleOnOffByBill: bool
    requestId: str
    transactionType: TransactionTypeEnum
    walletId: str
    bankBin: str
    bankName: BankNameEnum
    merchantId: float
    redirectUrl: str
    webhookUrl: str


class OpenApiConfirmVAOuputDto(TypedDict, total=False):
    accountType: BankAccountTypeEnum
    bankName: BankNameEnum
    accountNumber: str
    vaAccountNumber: str
    shopId: float


class OpenApiBankConfirmVAInputDto(TypedDict, total=False):
    merchantId: float  # optional
    confirmId: str
    otpNumber: str
    bankName: BankNameEnum  # optional
    bankBin: str  # optional


class BankDeleteVAOutputDto(TypedDict, total=False):
    confirmId: str
    authorizeLink: str


class OpenApiRegisterNotifyDto(TypedDict, total=False):
    merchantId: float  # optional
    vaAccountNumber: str
    bankBin: str  # optional
    bankName: BankNameEnum  # optional


class Boolean(TypedDict, total=False):
    pass


EventUrlItemType = Literal['shop', 'accountNumber', 'all', 'merchant']


class UpdateWebhookNotificationDto(TypedDict, total=False):
    webhookUrl: str  # optional
    vaAccountNumber: str  # optional
    targetId: float  # optional
    type: EventUrlItemType  # optional
    isActive: bool


class String(TypedDict, total=False):
    pass


BankLinkSessionTypeEnum = Literal['bank-link', 'bank-config', 'account-config']


class CreateBankLinkSessionInputDto(TypedDict, total=False):
    isSandbox: bool
    merchantId: float
    shopId: float
    merchantAccountNumberId: float
    allowedBanks: List[BankNameEnum]
    disallowedBanks: List[BankNameEnum]
    bankName: BankNameEnum
    defaultBankName: BankNameEnum
    bankAccountType: BankAccountTypeEnum
    type: BankLinkSessionTypeEnum
    metadata: str
    redirectUrl: str
    isEnableQRScan: bool


class OpenApiReadSecurityCodeDto(TypedDict, total=False):
    merchantId: float  # optional
    uuid: str


DeviceTypeEnum = Literal['app-tingee', 'tingee-box-f1', 'tingee-box-2a', 'tingee-box-2as', 'tingee-box-s1', 'tingee-box-3ls', 'tingee-box-3pro', 'tingee-box-3vn', 'tingee-box-3vna', 'tingee-box-4ls', 'tingee-box-5s', 'tingee-box-5sa', 'tingee-box-6ls', 'tingee-box-6pro', 'tingee-box-6xs', 'vn-50', 'loa-pay', 'trusted-pay', 'pay-alert', 'tingee-box-3vn-mbb', 'tingee-box-3pro-mbb', 'tingee-box-3pro-x', 'tingee-box-max', 'tingee-box-8pro']


class SendNotifyTingeeBoxDto(TypedDict, total=False):
    type: DeviceTypeEnum
    uuid: str


class OpenApiAddDeviceToShop(TypedDict, total=False):
    uuid: str
    securityCode: str
    appType: AppTypeEnum
    masterMerchantId: float  # optional
    merchantId: float  # optional
    vaAccountNumbers: List[str]  # optional
    shopIds: List[float]  # optional


class OpenApiShopLinkToDeviceDto(TypedDict, total=False):
    shopName: str
    shopId: float  # optional
    isLinkToDevice: bool
    fullAddress: str
    vaAccountNumber: str  # optional


class OpenApiUpdateShopDeviceLinkDto(TypedDict, total=False):
    uuid: str
    appType: AppTypeEnum
    shopsLinkToDeviceDtos: List[OpenApiShopLinkToDeviceDto]
    type: DeviceTypeEnum  # optional
    merchantId: float  # optional


class OpenApiPrintReceiptItemDto(TypedDict, total=False):
    name: str
    quantity: float
    unitPrice: float
    code: str  # optional
    unit: str  # optional
    lineDiscount: float  # optional
    promotionLabel: str  # optional
    taxPercent: float  # optional
    taxValue: float  # optional


class OpenApiPrintDataDto(TypedDict, total=False):
    templateType: Literal['1', '2']  # optional
    lineWidth: float  # optional
    qrAlignment: Literal['0', '1', '2']  # optional
    logo: Literal['printer_receipt_logo', 'printer_receipt_logo2', 'printer_receipt_logo3', 'printer_receipt_logo4', 'rintest']  # optional
    title: str  # optional
    storeName: str
    branchName: str  # optional
    address: str  # optional
    hotline: str  # optional
    orderCode: str  # optional
    invoiceNo: str  # optional
    customerName: str  # optional
    customerId: str  # optional
    sellerAddressLines: List[str]  # optional
    taxCode: str  # optional
    channelName: str  # optional
    employeeCode: str  # optional
    createdAt: str  # optional
    items: List[OpenApiPrintReceiptItemDto]
    totalAmount: float
    discount: float  # optional
    vatReduction: float  # optional
    paidAmount: float  # optional
    customerPaid: float  # optional
    paymentMethodLabel: str  # optional
    paymentAmount: float  # optional
    invoiceStage: Literal['PRE_PAYMENT', 'POST_PAYMENT']  # optional
    changeAmount: float  # optional
    qrCode: str  # optional
    qrHint: str  # optional
    barcode: str  # optional
    footerNote: str  # optional
    note: str  # optional
    bankAccountName: str  # optional
    bankAccountNo: str  # optional
    bankName: str  # optional
    voiceFile: float  # optional
    copies: float  # optional


class OpenApiReadAmountDto(TypedDict, total=False):
    merchantId: float  # optional
    uuid: str
    transactionId: str
    amount: float
    bankBin: str  # optional
    firstDisplayText: str  # optional
    secondDisplayText: str  # optional
    thirdDisplayText: str  # optional
    playSound: bool  # optional
    isPrint: bool  # optional
    printData: OpenApiPrintDataDto  # optional


class OpenApiShowQRCodeDto(TypedDict, total=False):
    merchantId: float  # optional
    uuid: str  # optional
    vaAccountNumber: str  # optional
    amount: float
    qrCode: str
    bankBin: str  # optional
    bankName: BankNameEnum  # optional
    deviceType: DeviceTypeEnum  # optional
    firstText: str  # optional
    secondText: str  # optional
    thirdText: str  # optional
    showTime: float  # optional
    isStaticQr: bool  # optional
    playSound: bool  # optional


class OpenApiClearDeviceScreenDto(TypedDict, total=False):
    merchantId: float  # optional
    uuid: str


class OpenApiGetDevicesLinkToShopOrVA(TypedDict, total=False):
    merchantId: float
    vaAccountNumber: str
    shopId: float


DeviceStatusEnum = Literal['waiting-progressing', 'refuse', 'approved']


class DeviceInfoDto(TypedDict, total=False):
    pass


class ShopInfoDto(TypedDict, total=False):
    name: str
    id: float


class DeviceDto(TypedDict, total=False):
    id: float  # optional
    creationTime: str  # optional
    creatorUserId: float  # optional
    lastModificationTime: str  # optional
    lastModifierUserId: float  # optional
    deleterUserId: float  # optional
    type: DeviceTypeEnum
    uuid: str
    name: str
    system: str  # optional
    systemVersion: str  # optional
    merchantId: float  # optional
    assignedAgentId: float  # optional
    merchantPhoneNumber: str  # optional
    employeeName: str  # optional
    firebaseToken: str  # optional
    status: DeviceStatusEnum
    deviceInfoDto: DeviceInfoDto  # optional
    useDate: str  # optional
    securityCode: str  # optional
    warrantyDate: str  # optional
    selectedBankNames: List[BankNameEnum]  # optional
    serialNumber: str  # optional
    userReferralAncestorIds: str  # optional
    userReferralLevel: float  # optional
    deviceDistributorAncestorIds: str  # optional
    deviceDistributorLevel: float  # optional
    masterMerchantId: float
    expirationDate: str  # optional
    latestReferralCode: str  # optional
    merchantName: str  # optional
    shopDtos: List[ShopInfoDto]  # optional
    agentName: str  # optional
    agentId: float  # optional
    simPhoneNumber: str  # optional
    simSerialNumber: str  # optional
    simProvider: str  # optional
    simPlan: str  # optional
    simExpirationDate: str  # optional
    simActivationDate: str  # optional


class OpenApiGetPagingDeviceInputDto(TypedDict, total=False):
    filter: str  # optional
    sorting: str  # optional
    skipCount: float  # optional
    maxResultCount: float  # optional
    merchantId: float
    type: DeviceTypeEnum  # optional


class OpenApiGenerateAndShowDynamicQrCodeDto(TypedDict, total=False):
    merchantId: float  # optional
    vaAccountNumber: str
    qrCodeType: QRCodeTypeEnum
    bankBin: str  # optional
    bankName: BankNameEnum  # optional
    name: str  # optional
    amount: float  # optional
    purpose: str  # optional
    expireInMinute: float  # optional
    extraInfo: str  # optional
    uuid: str
    deviceType: DeviceTypeEnum  # optional
    firstText: str  # optional
    secondText: str  # optional
    thirdText: str  # optional
    showTime: float  # optional
    playSound: bool  # optional
    readAmountAfterPay: bool  # optional


class OpenApiPrintReceiptDto(TypedDict, total=False):
    templateType: Literal['1', '2']  # optional
    lineWidth: float  # optional
    qrAlignment: Literal['0', '1', '2']  # optional
    logo: Literal['printer_receipt_logo', 'printer_receipt_logo2', 'printer_receipt_logo3', 'printer_receipt_logo4', 'rintest']  # optional
    title: str  # optional
    storeName: str
    branchName: str  # optional
    address: str  # optional
    hotline: str  # optional
    orderCode: str  # optional
    invoiceNo: str  # optional
    customerName: str  # optional
    customerId: str  # optional
    sellerAddressLines: List[str]  # optional
    taxCode: str  # optional
    channelName: str  # optional
    employeeCode: str  # optional
    createdAt: str  # optional
    items: List[OpenApiPrintReceiptItemDto]
    totalAmount: float
    discount: float  # optional
    vatReduction: float  # optional
    paidAmount: float  # optional
    customerPaid: float  # optional
    paymentMethodLabel: str  # optional
    paymentAmount: float  # optional
    invoiceStage: Literal['PRE_PAYMENT', 'POST_PAYMENT']  # optional
    changeAmount: float  # optional
    qrCode: str  # optional
    qrHint: str  # optional
    barcode: str  # optional
    footerNote: str  # optional
    note: str  # optional
    bankAccountName: str  # optional
    bankAccountNo: str  # optional
    bankName: str  # optional
    voiceFile: float  # optional
    copies: float  # optional
    merchantId: float  # optional
    uuid: str


class OpenApiNfcCommandDto(TypedDict, total=False):
    merchantId: float  # optional
    uuid: str
    enableNfc: bool  # optional
    playSound: bool  # optional
    nfcUrl: str  # optional
    nfcPackageName: str  # optional


DeviceNotifyOrderFoodNameEnum = Literal['befood', 'shopeefood', 'xanhsmfood', 'greensmfood', 'grabfood', 'ahamove', 'other']


class OpenApiDeviceNotifyOrderDto(TypedDict, total=False):
    merchantId: float  # optional
    uuid: str
    foodName: DeviceNotifyOrderFoodNameEnum
    amount: float  # optional


class OpenApiDeviceFeaturesDto(TypedDict, total=False):
    readAmount: bool
    showStaticQrCode: bool
    showDynamicQrCode: bool
    printReceipt: bool


class OpenApiDeviceFeaturesOutputDto(TypedDict, total=False):
    uuid: str
    type: DeviceTypeEnum
    features: OpenApiDeviceFeaturesDto


class OpenApiGetDeviceFeaturesDto(TypedDict, total=False):
    uuid: str


class OpenApiResetDeviceDto(TypedDict, total=False):
    uuid: str
    phoneNumber: str  # optional
    accountNumber: str  # optional
    isBankRequest: bool  # optional


class OpenApiCreateOrUpdateShopOutputDto(TypedDict, total=False):
    shopId: float


class SendNotifyTelegramDto(TypedDict, total=False):
    chatId: float


class SendNotifyLarkDto(TypedDict, total=False):
    urlWebhook: str


ZaloTypeEnum = Literal['phone-number', 'group']


class SendNotifyZaloDto(TypedDict, total=False):
    type: ZaloTypeEnum
    name: str


class SendNotifyPlatformDto(TypedDict, total=False):
    telegramDtos: List[SendNotifyTelegramDto]
    larkDtos: List[SendNotifyLarkDto]
    zaloDtos: List[SendNotifyZaloDto]
    tingeeBoxDtos: List[SendNotifyTingeeBoxDto]


ShopCreationSourceEnum = Literal['tingee-baas', 'tingee-merchant', 'tingee-box']


class OpenApiCreateOrUpdateShopDto(TypedDict, total=False):
    id: float  # optional
    name: str
    email: str  # optional
    phoneNumber: str  # optional
    provinceId: str  # optional
    districtId: str  # optional
    communeId: str  # optional
    address: str  # optional
    fullAddress: str  # optional
    sendNotifyPlatformDto: SendNotifyPlatformDto  # optional
    isActive: bool
    status: Literal['notConnectedDevice', 'delivering', 'delivered', 'connectedDevice', 'linkedVa', 'linkedVaNoDevice']  # optional
    userReferralAncestorIds: str  # optional
    userReferralLevel: float  # optional
    deviceDistributorAncestorMap: str  # optional
    creationSource: ShopCreationSourceEnum  # optional
    isForceDisableNotify: bool  # optional
    isOpenNotify: bool  # optional
    merchantId: float  # optional


class OpenApiGetShopPagedOuputDto(TypedDict, total=False):
    id: float
    isActive: bool
    name: str
    address: str


class OpenApiGetShopPagedInputDto(TypedDict, total=False):
    filter: str
    sorting: str
    skipCount: float
    maxResultCount: float
    merchantId: float


class OpenApiDeepLinkDto(TypedDict, total=False):
    merchantId: float  # optional
    type: str
    qrCode: str  # optional
    redirectUrl: str  # optional
    callbackUrl: str  # optional
    bankBin: str
    destinationBankBin: str  # optional
    accountName: str  # optional
    accountNumber: str  # optional
    amount: float  # optional
    content: str  # optional
    platform: float  # optional
    billNumber: str  # optional


class OpenApiTransactionPagedInputDto(TypedDict, total=False):
    filter: str  # optional
    sorting: str  # optional
    skipCount: float  # optional
    maxResultCount: float  # optional
    merchantId: float  # optional
    shopIds: List[float]  # optional
    vaAccountNumbers: List[str]  # optional
    bankBin: str  # optional
    billId: str  # optional
    startTime: str
    endTime: str


class MerchantBankConfigPagedOutputDto(TypedDict, total=False):
    id: float
    creationTime: str  # optional
    creatorUserId: float  # optional
    lastModificationTime: str  # optional
    lastModifierUserId: float  # optional
    deleterUserId: float  # optional
    merchantId: float
    accountType: BankAccountTypeEnum
    configDto: Dict[str, Any]  # optional
    bankBin: str  # optional
    bankName: BankNameEnum  # optional


class OpenApiMerchantBankConfigPagedInputDto(TypedDict, total=False):
    filter: str
    sorting: str
    skipCount: float
    maxResultCount: float
    accountType: BankAccountTypeEnum
    merchantId: float
    bankBin: str
    bankName: BankNameEnum


class BIDVConfigDto(TypedDict, total=False):
    vaPrefix: str
    bankPartnerId: str
    accountNumber: str
    accountName: str


class CTGConfigDto(TypedDict, total=False):
    accountNumber: str
    accountName: str
    vaPrefix: str


class ACBConfigBusinessDto(TypedDict, total=False):
    accountNumber: str
    accountName: str
    vaPrefix: str
    mobile: str
    acbUserId: str


class MSBConfigBusinessDto(TypedDict, total=False):
    accountNumber: str
    vaPrefix: str
    mobile: str
    merchantId: str
    terminalId: str
    accessCode: str
    referralCode: str


class BaoKimConfigDto(TypedDict, total=False):
    mid: str
    accountName: str
    walletId: str
    privateKey: str


class HDBConfigDto(TypedDict, total=False):
    secretKey: str
    merchantId: str
    terminalId: str
    accountNumber: str
    accountName: str


class OpenApiBankCreateOrUpdateConfigDto(TypedDict, total=False):
    bidvConfigDto: BIDVConfigDto  # optional
    ctgConfigDto: CTGConfigDto  # optional
    acbConfigDto: ACBConfigBusinessDto  # optional
    msbConfigDto: MSBConfigBusinessDto  # optional
    baokimConfigDto: BaoKimConfigDto  # optional
    hdbConfigDto: HDBConfigDto  # optional
    accountType: BankAccountTypeEnum
    id: float  # optional
    otpNumber: str  # optional
    confirmId: str  # optional
    bankBin: str  # optional
    bankName: BankNameEnum  # optional
    merchantId: float  # optional


class OpenApiDeleteConfigDto(TypedDict, total=False):
    otpNumber: str  # optional
    confirmId: str  # optional
    id: float
    merchantId: float  # optional


class OpenApiCreateBankVAOutputDto(TypedDict, total=False):
    confirmId: str


class OpenApiConfigAccountBusinessDto(TypedDict, total=False):
    bankName: BankNameEnum  # optional
    accountNumber: str  # optional
    accountName: str  # optional
    mobile: str  # optional
    vaPrefix: str  # optional
    merchantId: float  # optional
    acbUserId: str
    bankBin: str  # optional


class OpenApiDeleteConfigBusinessDto(TypedDict, total=False):
    accountType: BankAccountTypeEnum
    configRemove: ACBConfigBusinessDto  # optional
    merchantId: float  # optional
    bankBin: str  # optional
    bankName: BankNameEnum  # optional


class OpenApiMerchantIdDto(TypedDict, total=False):
    merchantId: float


MerchantBaasTypeEnum = Literal['trial', 'trial-extended', 'customer', 'cancelled', 'unclassified']


class BankLinkConfigDto(TypedDict, total=False):
    phone: str
    email: str
    brandName: str
    redirectUrl: str


MerchantCreationSourceEnum = Literal['tingee-baas', 'tingee-merchant']


class OpenApiCreateMerchantDto(TypedDict, total=False):
    id: float  # optional
    code: str  # optional
    name: str
    email: str  # optional
    phoneNumber: str
    website: str  # optional
    businessSectorIds: List[float]  # optional
    provinceId: str  # optional
    districtId: str  # optional
    communeId: str  # optional
    address: str  # optional
    fullAddress: str  # optional
    referralCode: str  # optional
    baasType: MerchantBaasTypeEnum  # optional
    bankLinkConfigDto: BankLinkConfigDto  # optional
    assignedUserId: float  # optional
    creationSource: MerchantCreationSourceEnum  # optional
    password: str  # optional
    appType: AppTypeEnum  # optional
    requirePasswordChange: bool  # optional


class EventUrlItemDto(TypedDict, total=False):
    url: str
    type: EventUrlItemType
    ids: List[str]  # optional


class FileUploadDto(TypedDict, total=False):
    fileLogId: str
    path: str


class OCBConfigDto(TypedDict, total=False):
    clientId: str
    clientSecret: str  # optional
    pathCertKey: FileUploadDto  # optional
    pathPrivateKey: FileUploadDto  # optional
    userName: str
    accountName: str
    password: str  # optional
    vaPrefix: str  # optional
    vaPrefixForDynamicQR: str  # optional
    accountNumbers: List[str]  # optional


class MBBConfigDto(TypedDict, total=False):
    accountNumber: str
    accountName: str
    identity: str
    mobile: str


class ShinhanConfigDto(TypedDict, total=False):
    vaPrefix: str
    clientId: str
    clientSecret: str  # optional
    pathPublicKey: FileUploadDto  # optional
    pathPrivateKey: FileUploadDto  # optional
    accountNumber: str
    accountName: str


class VIBConfigDto(TypedDict, total=False):
    vaPrefix: str
    pathPublicKey: FileUploadDto  # optional
    pathPrivateKey: FileUploadDto  # optional
    basicAuthToken: str
    cif: str
    clientId: str
    clientSecret: str
    accountNumber: str
    vaCharactersNumber: float


class ACBConfigDto(TypedDict, total=False):
    businessAccounts: List[ACBConfigBusinessDto]
    businessHouseholdAccounts: List[ACBConfigBusinessDto]


class VPBConfigBusinessDto(TypedDict, total=False):
    accountNumber: str
    accountName: str
    merchantId: str
    terminalId: str


class VPBConfigDto(TypedDict, total=False):
    businessAccounts: List[VPBConfigBusinessDto]
    businessHouseholdAccounts: List[VPBConfigBusinessDto]


class VCBConfigBusinessDto(TypedDict, total=False):
    accountNumber: str
    accountName: str
    merchantId: str
    terminalId: str


class VCBConfigDto(TypedDict, total=False):
    businessAccounts: List[VCBConfigBusinessDto]
    businessHouseholdAccounts: List[VCBConfigBusinessDto]


class BankConfigDto(TypedDict, total=False):
    ocbConfigDtos: List[OCBConfigDto]
    mbbConfigDtos: List[MBBConfigDto]
    bidvConfigDtos: List[BIDVConfigDto]
    shinhanConfigDtos: List[ShinhanConfigDto]
    vibConfigDtos: List[VIBConfigDto]
    ctgConfigDtos: List[CTGConfigDto]
    acbConfigDto: ACBConfigDto
    vpbConfigDto: VPBConfigDto
    vcbConfigDto: VCBConfigDto
    hdbConfigDto: HDBConfigDto
    baokimConfigDto: BaoKimConfigDto


class BNPLConfigDto(TypedDict, total=False):
    baokimConfigDto: BaoKimConfigDto


class OnePayConfigDto(TypedDict, total=False):
    merchantId: str
    signingKey: str
    verifyKey: str
    accessCode: str
    hashCode: str
    callbackUrl: str


class DirectDebitConfigDto(TypedDict, total=False):
    onePayConfigDto: OnePayConfigDto


class MerchantPackageInfo(TypedDict, total=False):
    packageName: str
    expirationDate: str


class MerchantDto(TypedDict, total=False):
    id: float
    creationTime: str  # optional
    isPrepaidCollectionOnMerchant: bool  # optional
    code: str  # optional
    name: str
    email: str  # optional
    phoneNumber: str
    website: str  # optional
    businessSectorIds: List[float]  # optional
    provinceId: str  # optional
    districtId: str  # optional
    communeId: str  # optional
    address: str  # optional
    fullAddress: str  # optional
    clientId: str  # optional
    secretToken: str  # optional
    eventUrl: str  # optional
    eventUrls: List[EventUrlItemDto]  # optional
    isLockEvent: bool  # optional
    bankConfigDto: BankConfigDto  # optional
    bnplConfigDto: BNPLConfigDto  # optional
    directDebitConfigDto: DirectDebitConfigDto  # optional
    sendNotifyPlatformDto: SendNotifyPlatformDto  # optional
    isOrganizationUnit: bool  # optional
    referralCode: str  # optional
    userReferralAncestorIds: str  # optional
    userReferralLevel: float  # optional
    deviceDistributorAncestorMap: str  # optional
    isMasterMerchant: bool  # optional
    baasType: MerchantBaasTypeEnum  # optional
    bankLinkConfigDto: BankLinkConfigDto  # optional
    assignedUserId: float  # optional
    creationSource: MerchantCreationSourceEnum
    merchantPackages: List[MerchantPackageInfo]  # optional
    masterMerchantNames: str  # optional
    isPostpaid: bool  # optional
    overdraftLimit: float  # optional
    isLockoutEnabled: bool  # optional
    assignedUserName: str  # optional


class OpenApiGetPagingMerchantsDto(TypedDict, total=False):
    filter: str
    sorting: str
    skipCount: float
    maxResultCount: float


class OpenApiRegisterDto(TypedDict, total=False):
    requestId: str
    bankBin: str  # optional
    accountName: str  # optional
    email: str  # optional
    phone: str
    returnUrl: str
    isSandbox: bool  # optional


DirectDebitTransactionStatusEnum = Literal['success', 'failure', 'pending', 'pending-confirm', 'confirmed-and-sent-to-direct-debit', 'insufficient-balance', 'exceed-daily-limit', 'refunded']


class PaymentBillResponseDto(TypedDict, total=False):
    code: str
    status: DirectDebitTransactionStatusEnum
    transactionCode: str
    isSentConfirmEmail: bool
    isSentConfirmZalo: bool
    returnUrl: str


DirectDebitPartnerEnum = Literal['one-pay']


class OpenApiPaymentBillDto(TypedDict, total=False):
    requestId: str
    clientId: str  # optional
    subscriptionId: str
    amount: str
    description: str
    expirationTime: str  # optional
    signature: str  # optional
    token: str  # optional
    additionalData: Dict[str, Any]  # optional
    tokenRef: str  # optional
    partnerCode: DirectDebitPartnerEnum
    accountNumber: str  # optional
    serviceProviderName: str
    returnUrl: str  # optional


class DeleteSubscriptionOutputDto(TypedDict, total=False):
    confirmUrl: str
    code: str


class OpenApiDeleteSubscriptionDto(TypedDict, total=False):
    requestId: str
    returnUrl: str
    subscriptionId: str
    tokenRef: str


DirectDebitRefundStatusEnum = Literal['success', 'failure', 'Pending']


class RefundOutputDto(TypedDict, total=False):
    refundAmount: float
    transactionId: str
    status: DirectDebitRefundStatusEnum


class OpenApiRefundInputDto(TypedDict, total=False):
    subscriptionId: str
    tokenRef: str
    transactionId: str
    amount: float


class OpenApiEditConfirmBeforePaymentMethodDto(TypedDict, total=False):
    requestId: str
    returnUrl: str
    subscriptionId: str


DirectDebitStatusEnum = Literal['active', 'inactive']


class OpenApiSubscriptionStatusResponseDto(TypedDict, total=False):
    lastModificationTime: str  # optional
    lastModifierUserId: float  # optional
    email: str  # optional
    bankName: BankNameEnum
    accountName: str  # optional
    accountNumber: str
    phone: str
    confirmPaymentByEmail: bool
    confirmEmail: str  # optional
    confirmPaymentByZalo: bool
    confirmPhoneNumber: str
    tokenRef: str  # optional
    status: DirectDebitStatusEnum
    subscriptionId: str  # optional
    bankBin: str  # optional


class CustomerInfoDto(TypedDict, total=False):
    onepayAccountId: str
    name: str
    phone: str
    email: str  # optional


WebhookStatusEnum = Literal['success', 'failed', 'pending', 'insufficient-balance', 'exceed-daily-limit', 'confirm-va-success', 'confirm-va-failed', 'delete-va-success', 'delete-va-failed', 'bank-link-success', 'bank-link-failed']


class OpenApiPaymentTransactionStatusResponseDto(TypedDict, total=False):
    transactionId: str  # optional
    subscriptionId: str  # optional
    customerKey: str  # optional
    tokenRef: str
    bankBin: str
    customer: CustomerInfoDto
    accountNumber: str  # optional
    accountName: str  # optional
    code: str  # optional
    amount: float  # optional
    currency: str  # optional
    content: str  # optional
    transactionDate: str  # optional
    status: WebhookStatusEnum


class OpenApiPaymentTransactionsPagedOutputDto(TypedDict, total=False):
    transactionId: str
    code: str
    bankName: BankNameEnum
    bankBin: str
    amount: str
    content: str
    accountNumber: str
    transactionDate: str
    subscriptionId: str
    tokenRef: str
    status: DirectDebitTransactionStatusEnum
    additionalData: Dict[str, Any]  # optional


EInvoiceProviderEnum = Literal['x-cyber', 'hilo', 's-invoice', 'misa', 'bkav']


EInvoiceServiceEnum = Literal['output-invoice', 'input-invoice']


class GetPagingEInvoiceAccountOutputDto(TypedDict, total=False):
    id: float
    creationTime: str  # optional
    merchantId: float
    masterMerchantId: float
    provider: EInvoiceProviderEnum
    taxCode: str
    username: str
    password: str
    isDefault: bool  # optional
    isActive: bool  # optional
    services: List[EInvoiceServiceEnum]  # optional
    merchantName: str  # optional
    masterMerchantName: str  # optional


class GetPagingEInvoiceAccountInputDto(TypedDict, total=False):
    filter: str
    sorting: str
    skipCount: float
    maxResultCount: float
    provider: EInvoiceProviderEnum
    isDefault: bool
    isActive: bool
    merchantId: float
    masterMerchantId: float


class CreateOrUpdateEInvoiceAccountDto(TypedDict, total=False):
    masterMerchantId: float  # optional
    provider: EInvoiceProviderEnum
    taxCode: str
    username: str
    password: str
    isDefault: bool  # optional
    isActive: bool  # optional
    id: float  # optional
    merchantId: float  # optional
    services: List[Literal['output-invoice', 'input-invoice']]  # optional


class DeleteEInvoiceAccountDto(TypedDict, total=False):
    id: float
    merchantId: float  # optional


class EInvoiceProviderDto(TypedDict, total=False):
    code: EInvoiceProviderEnum
    name: str
    description: str
    urlLogo: str
    lookupUrlPattern: str


class DownloadInvoiceOutputDto(TypedDict, total=False):
    invoiceCode: str
    pdfBase64: str  # optional


class InvoiceItemDto(TypedDict, total=False):
    itemCode: str  # optional
    itemName: str
    unitName: str  # optional
    quantity: str
    unitPrice: str
    discount: str  # optional
    discountAmount: str  # optional
    totalBeforeTax: str  # optional
    taxRateCode: str
    taxAmount: str  # optional
    totalAfterTax: str  # optional
    itemType: float  # optional
    adjustmentType: float  # optional


class TaxRateSummaryDto(TypedDict, total=False):
    taxRateCode: str
    totalTaxableAmount: str  # optional
    taxAmount: str  # optional


class CreateInvoiceDto(TypedDict, total=False):
    merchantId: float  # optional
    accountId: float  # optional
    invoiceType: str  # optional
    invoicePattern: str
    invoiceSeries: str
    invoiceCode: str
    invoiceDate: str
    buyerTaxCode: str  # optional
    buyerIdentity: str  # optional
    buyerIdType: str  # optional
    buyerName: str  # optional
    buyerLegalName: str  # optional
    buyerAddress: str  # optional
    buyerPhone: str  # optional
    buyerEmail: str  # optional
    buyerBankAccount: str  # optional
    buyerBankName: str  # optional
    paymentMethod: float  # optional
    paymentMethodName: str  # optional
    currency: str  # optional
    exchangeRate: str  # optional
    amountInWords: str  # optional
    note: str  # optional
    items: List[InvoiceItemDto]
    totalDiscount: str  # optional
    totalBeforeTax: str  # optional
    totalTax: str  # optional
    totalAfterTax: str  # optional
    taxRateSummaries: List[TaxRateSummaryDto]  # optional


class TrackingResultDto(TypedDict, total=False):
    invoiceCode: str
    trackingCode: str  # optional
    invoiceNumber: str  # optional
    reservationCode: str  # optional
    codeOfTax: str  # optional
    url: str  # optional


class GetInvoiceInfoQueryDto(TypedDict, total=False):
    merchantId: float  # optional
    accountId: float  # optional
    invoiceCode: str


class DownloadInvoiceQueryDto(TypedDict, total=False):
    merchantId: float  # optional
    accountId: float  # optional
    invoiceCode: str


class InvoiceTemplateOutputDto(TypedDict, total=False):
    invoicePattern: str
    invoiceSeries: str
    quota: float  # optional


class InvoiceTemplateInputDto(TypedDict, total=False):
    merchantId: float
    accountId: float
    provider: EInvoiceProviderEnum
    taxCode: str
    username: str
    password: str
    invoiceNoToCheck: float


class SendInvoiceEmailDto(TypedDict, total=False):
    merchantId: float  # optional
    accountId: float  # optional
    invoiceCode: str
    buyerName: str  # optional
    recipientEmail: str


class ConnectTCTRequestDto(TypedDict, total=False):
    merchantId: float
    accountId: float
    tctUsername: str
    tctPassword: str


class InputInvoiceBaseDto(TypedDict, total=False):
    merchantId: float
    accountId: float


class SyncIncomeInvoiceRequestDto(TypedDict, total=False):
    merchantId: float
    accountId: float
    fromDate: str
    toDate: str


class IncomeInvoiceListItemDto(TypedDict, total=False):
    id: float
    invoiceCode: str
    fileHistoryId: str
    invoiceNo: str
    invoicePattern: str
    invoiceSeries: str
    sellerName: str
    sellerTaxCode: str
    totalBeforeTax: float
    taxAmount: float
    totalAfterTax: float
    invoiceDate: str
    receivedDate: str
    invoiceStatus: float
    approvalStatus: float
    tctStatus: float
    invoiceType: float
    invoiceProperty: float
    importMethod: float
    orderNo: str
    note: Dict[str, Any]


class IncomeInvoiceListOutputDto(TypedDict, total=False):
    items: List[IncomeInvoiceListItemDto]
    totalCount: float


class GetIncomeInvoicesListRequestDto(TypedDict, total=False):
    merchantId: float
    accountId: float
    sellerTaxCode: str
    buyerTaxCode: str
    current: float
    approvedFromDate: str
    approvedToDate: str
    invoiceFromDate: str
    invoiceToDate: str
    receivedFromDate: str
    receivedToDate: str
    label: str
    page: float
    pageSize: float
    size: float
    invoiceNo: str
    invoiceProperty: float
    approvalStatus: float


class IncomeInvoiceItemDetailDto(TypedDict, total=False):
    id: float
    lineNumber: float
    itemName: str
    unitName: str
    quantity: float
    unitPrice: float
    totalBeforeTax: float
    taxRate: str
    taxAmount: float
    itemType: float
    isPromotion: bool


class IncomeInvoiceTaxRateSummaryDto(TypedDict, total=False):
    id: float
    taxRate: str
    taxAmount: float


class IncomeInvoiceDetailOutputDto(TypedDict, total=False):
    invoiceCode: str  # optional
    fileHistoryId: str  # optional
    invoiceName: str  # optional
    invoicePattern: str  # optional
    invoiceSeries: str  # optional
    invoiceNo: str  # optional
    invoiceDate: str  # optional
    approvedDate: str  # optional
    receivedDate: str  # optional
    paymentDate: str  # optional
    signedDate: str  # optional
    currency: str  # optional
    exchangeRate: float  # optional
    paymentMethod: str  # optional
    sellerName: str  # optional
    sellerTaxCode: str  # optional
    sellerAddress: str  # optional
    buyerName: str  # optional
    buyerTaxCode: str  # optional
    buyerAddress: str  # optional
    totalBeforeTax: float  # optional
    taxAmount: float  # optional
    discountAmount: float  # optional
    totalAfterTax: float  # optional
    amountInWords: str  # optional
    invoiceStatus: float  # optional
    approvalStatus: float  # optional
    invoiceType: float  # optional
    note: str  # optional
    items: List[IncomeInvoiceItemDetailDto]
    taxRateSummaries: List[IncomeInvoiceTaxRateSummaryDto]


class GetIncomeInvoiceDetailRequestDto(TypedDict, total=False):
    merchantId: float  # optional
    accountId: float  # optional
    invoiceCode: str


class IncomeInvoicePreviewBase64OutputDto(TypedDict, total=False):
    fileBase64: str


class GetIncomeInvoicePreviewBase64RequestDto(TypedDict, total=False):
    merchantId: float  # optional
    accountId: float  # optional
    invoiceCode: str


class OpenApiCreatePaymentLinkInputDto(TypedDict, total=False):
    merchantId: float  # optional
    orderId: str
    requestId: str
    amount: float
    currency: str  # optional
    expireInMinute: float  # optional
    description: str  # optional
    orderInfo: str  # optional
    bankBin: str  # optional
    vaAccountNumber: str  # optional
    returnUrl: str  # optional
    customerEmail: str  # optional
    paymentGroup: str  # optional

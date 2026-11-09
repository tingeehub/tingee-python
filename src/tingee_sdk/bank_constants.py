"""Bank constants (same as the other SDKs)."""

from enum import Enum
from typing import Dict, List, Optional, TypedDict

__all__ = [
    "BankNameEnum",
    "BankBinEnum",
    "BankAccountTypeEnum",
    "BankInfo",
    "BANKS_OBJECT",
    "BANKS",
    "get_bank_code",
    "get_bank_short_name",
    "get_bank_bin",
]


class BankNameEnum(str, Enum):
    OCB = "OCB"
    BIDV = "BIDV"
    MBB = "MBB"
    ACB = "ACB"
    VPB = "VPB"
    PGB = "PGB"
    VIB = "VIB"
    STB = "STB"
    CTG = "CTG"
    VCB = "VCB"
    AGRIBANK = "AGRIBANK"
    SHINHAN = "SHINHAN"
    COB = "COB"


class BankBinEnum(str, Enum):
    OCB = "970448"
    BIDV = "970418"
    MBB = "970422"
    ACB = "970416"
    VPB = "970432"
    PGB = "970430"
    VIB = "970441"
    STB = "970403"
    CTG = "970415"
    VCB = "970436"
    AGRIBANK = "970405"
    SHINHAN = "970424"
    COB = "970446"


class BankAccountTypeEnum(str, Enum):
    PersonalAccount = "personal-account"
    BusinessAccount = "business-account"
    BusinessHouseHoldAccount = "business-household-account"


class BankInfo(TypedDict):
    code: BankNameEnum
    name: str
    shortName: str
    bin: str


BANKS_OBJECT: Dict[BankNameEnum, BankInfo] = {
    BankNameEnum.VCB: {"code": BankNameEnum.VCB, "name": "Ngân hàng TMCP Ngoại Thương Việt Nam", "bin": "970436", "shortName": "Vietcombank"},
    BankNameEnum.CTG: {"code": BankNameEnum.CTG, "name": "Ngân hàng TMCP Công thương Việt Nam", "bin": "970415", "shortName": "VietinBank"},
    BankNameEnum.BIDV: {"code": BankNameEnum.BIDV, "name": "Ngân hàng TMCP Đầu tư và Phát triển Việt Nam", "bin": "970418", "shortName": "BIDV"},
    BankNameEnum.AGRIBANK: {"code": BankNameEnum.AGRIBANK, "name": "Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam", "bin": "970405", "shortName": "Agribank"},
    BankNameEnum.MBB: {"code": BankNameEnum.MBB, "name": "Ngân hàng TMCP Quân đội", "bin": "970422", "shortName": "MB Bank"},
    BankNameEnum.ACB: {"code": BankNameEnum.ACB, "name": "Ngân hàng TMCP Á Châu", "bin": "970416", "shortName": "ACB"},
    BankNameEnum.OCB: {"code": BankNameEnum.OCB, "name": "Ngân hàng TMCP Phương Đông", "bin": "970448", "shortName": "OCB Bank"},
    BankNameEnum.VPB: {"code": BankNameEnum.VPB, "name": "Ngân hàng TMCP Việt Nam Thịnh Vượng", "bin": "970432", "shortName": "VPBank"},
    BankNameEnum.STB: {"code": BankNameEnum.STB, "name": "Ngân hàng TMCP Sài Gòn Thương Tín", "bin": "970403", "shortName": "Sacombank"},
    BankNameEnum.VIB: {"code": BankNameEnum.VIB, "name": "Ngân hàng TMCP Quốc tế Việt Nam", "bin": "970441", "shortName": "VIB"},
    BankNameEnum.PGB: {"code": BankNameEnum.PGB, "name": "Ngân Hàng TMCP Thịnh vượng và Phát triển", "bin": "970430", "shortName": "PGBank"},
    BankNameEnum.SHINHAN: {"code": BankNameEnum.SHINHAN, "name": "Ngân hàng TNHH MTV Shinhan Việt Nam", "bin": "970424", "shortName": "Shinhan Bank"},
    BankNameEnum.COB: {"code": BankNameEnum.COB, "name": "Ngân hàng Hợp tác Xã Việt Nam", "bin": "970446", "shortName": "Co-opBank"},
}

BANKS: List[BankInfo] = list(BANKS_OBJECT.values())


def get_bank_code(bank_bin: str) -> Optional[BankNameEnum]:
    return next((x["code"] for x in BANKS if x["bin"] == bank_bin), None)


def get_bank_short_name(bank_bin: str) -> Optional[str]:
    return next((x["shortName"] for x in BANKS if x["bin"] == bank_bin), None)


def get_bank_bin(bank_name: BankNameEnum) -> Optional[str]:
    return next((x["bin"] for x in BANKS if x["code"] == bank_name), None)

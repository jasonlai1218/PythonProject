from enum import Enum


class EventDataFrameColumn(Enum):
    ID = "id"
    STATE = "state"
    CONTRACT_ID = "contract_id"
    ECID = "ecid"
    MID = "mid"
    ORDER_ID = "order_id"
    ORDER_TIME = "order_time"
    TRANSACTION_ID = "transaction_id"
    DATE = "dt"


class TestDataFrameColumn(Enum):
    AA = "aa"
    BB = "bb"


class ContractDataFrameMagicValue(Enum):
    INT_AS_NULL = -100


class ContractDataFrameColumn(Enum):
    OPERATION_LOG = "operation_log"
    USER_UPPER_LIMIT = "user_upper_limit"
from enum import Enum
from enum import unique


@unique
class Status(Enum):
    success = '0000'
    emptyError = '0001'
    mysqlError = '0003'
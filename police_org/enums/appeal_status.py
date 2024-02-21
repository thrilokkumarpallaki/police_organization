from . import *


class AppealStatus(enum.Enum):
    CLOSED = 1
    CAN_APPEAL = 2
    IN_APPEAL = 3

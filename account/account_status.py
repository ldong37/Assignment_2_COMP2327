from enum import Enum   
from decimal import Decimal

class AccountStatus(Enum):
    INACTIVE = 0
    ACTIVE = 1
    SUSPENDED = 2 
    CLOSED = 3
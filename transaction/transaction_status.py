"""
Enumeration representing the status of a transaction.
List 3 lifecycle states are Pending, Processed and Failed
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from enum import Enum

class TransactionStatus (Enum):
    """
    Represent the 3 lifecycle states of a bank transaction
    Attributes:
        PENDING: The transaction is pending and has not been processed yet.
        PROCESSED: The transaction has been successfully processed.
        FAILED: The transaction has failed to process.
    """
    
    PENDING = 1
    PROCESSED = 2
    FAILED = 3
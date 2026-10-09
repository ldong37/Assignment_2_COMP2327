"""
Abstract base class for a bank account transactions.
This class defines the validation rules and defines the abstract interface that subclasses must implement to represent a bank account transaction.
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


from account.bank_account import BankAccount
from .transaction_status import TransactionStatus

class Transaction(ABC):
    """
    Abstract base class for a bank account transaction.
    This class defines the validation rules and defines the abstract interface that subclasses must implement to represent a bank account transaction.
    """

    def __init__(self, 
                 transaction_id: str,
                 amount: Decimal, 
                 account: BankAccount,
    ) -> None:
        """
        Initialize a Transaction object with the specified amount and account.
        The transaction status is set to PENDING by default.

        Args:
            transaction_id (str): The unique identifier for the transaction.
            amount (Decimal): The amount of money involved in the transaction.
            account (BankAccount): The bank account associated with the transaction.

        Raises:
            ValueError: If the amount is not a positive number.
            ValueError: If the transaction_id is a blank string.
        """
        if transaction_id.strip() == "":
            raise ValueError("Transaction ID cannot be blank.")

        if amount <= Decimal ("0"):
            raise ValueError("Transaction amount must be a positive number.")

        self._transaction_id: str = transaction_id
        self._amount: Decimal = amount
        self._status: TransactionStatus = TransactionStatus.PENDING
        self._account: BankAccount = account

    
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
            raise ValueError("transactionid cannot be blank.")

        if amount <= Decimal ("0"):
            raise ValueError("amount must be greater than zero")

        self._transaction_id: str = transaction_id
        self._amount: Decimal = amount
        self._status: TransactionStatus = TransactionStatus.PENDING
        self._account: BankAccount = account

    @property 
    def transaction_id(self) -> str:
       """
       Get the unique identifier for the transaction.

       Returns:
       str: The transaction ID.
       """
       return self._transaction_id

    @property
    def amount(self) -> Decimal:
       """
       Get the amount of money involved in the transaction.

       Returns:
        Decimal: The transaction amount.
       """
       return self._amount

    @property
    def status(self) -> TransactionStatus:
       """
       Get the status of the transaction.

       Returns:
        TransactionStatus: The transaction status.
       """
       return self._status

    @status.setter
    def status(self, value: TransactionStatus) -> None:
       """
       Set the status of the transaction.

       Args:
         Value (TransactionStatus): The new status to set for the transaction.
       """
       self._status = value


    @property
    def account(self) -> BankAccount:
       """
       Get the bank account associated with the transaction.

       Returns:
        BankAccount: The associated bank account.
       """
       return self._account

    @property
    @abstractmethod
    def fees(self) -> Decimal:
       """
       Abstract property to get the fees associated with the transaction.
       Subclasses must implement this property to calculate and return the fees.

       Returns:
        Decimal: The fees associated with the transaction.
       """
       raise NotImplementedError


    @abstractmethod
    def process(self) -> None:
       """
       Abstract method to process the transaction.
       Subclasses must implement this method to define the specific processing logic for the transaction.
       This method should update the transaction status accordingly.

       Raises:
          NotImplementedError: If the method is not implemented in a subclass.
       """
       raise NotImplementedError
    

    @staticmethod
    def _format_currency(value: Decimal) -> str:
        """
        Format a Decimal amount as a currency string with two decimal places.

        Args:
            value (Decimal): The amount to format.

        Returns:
            str: The formatted currency string.
        """
        rounded_value = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return f"${value:,.2f}"


    def __str__(self) -> str:
        """
        Return a string representation of the transaction.

        Returns:
            str: A string representation of the transaction, including its ID, amount, status, and associated account.
        """
        return (f"ID: {self.transaction_id}"
                f"Amount: {self._format_currency(self.amount)}" 
                f"Status: {self.status.name}" 
                f"Account: {self.account.account_number}"
        )
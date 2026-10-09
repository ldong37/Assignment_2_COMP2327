"""
This module contains the CreditCardTransaction class, which represents a credit card transaction in the system. It includes methods for processing payments, validating card information, and handling transaction statuses.
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from decimal import Decimal
from account.bank_account import BankAccount
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus


class CreditCardTransaction(Transaction):
    """
    Concrete implementation of a credit card transaction.
    This class represents a specific type of transaction that involves processing payments using a credit card.
    It includes methods for executing the payment, validating the card information, and handling any errors that may arise during the process.
    """
    FEE_RATE: Decimal = Decimal("0.02")  # Fee rate as a percentage of the transaction amount

    def __init__(self, 
                 transaction_id: str,
                 amount: Decimal, 
                 account: BankAccount, 
                 authorization_code: str) -> None:
        """
        Initialize a CreditCardTransaction object with the specified amount, account, and authorization code.
        The transaction status is set to PENDING by default.

        Args:
            transaction_id (str): The unique identifier for the transaction.
            amount (Decimal): The amount of money to be charged to the credit card.
            account (BankAccount): The bank account associated with the credit card.
            authorization_code (str): The authorization code for the transaction.

        Raises:
            ValueError: If the amount is not a positive number.
            ValueError: If the account is None.
            ValueError: If the authorization code is invalid or blank.
        """
        super().__init__(transaction_id, amount, account)
        self._authorization_code: str = authorization_code

    @property
    def authorization_code(self) -> str:
        """
        Get the authorization code for the credit card transaction.

        Returns:
            str: The authorization code.
        """
        return self._authorization_code



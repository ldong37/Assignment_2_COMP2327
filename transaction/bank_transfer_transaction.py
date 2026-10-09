"""
Concrete implementation of a bank transfer transaction. This class represents a specific type of transaction that involves transferring funds from one bank account to another. It includes methods for executing the transfer, validating the transaction details, and handling any errors that may arise during the process.
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from decimal import Decimal
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus

class BankTransferTransaction(Transaction):
    """
    Concrete implementation of a bank transfer transaction.
    This class represents a specific type of transaction that involves transferring funds from one bank account to another.
    It includes methods for executing the transfer, validating the transaction details, and handling any errors that may arise during the process.
    """
    BASE_FEE: Decimal = Decimal("1.00")  # Base fee for the transaction
    FEE_RATE: Decimal = Decimal("0.007")  # Fee rate as a percentage of the transaction amount

    def __init__(self, 
                 transaction_id: str,
                 amount: Decimal, 
                 account: BankAccount, 
                 target_account: BankAccount) -> None:
        """
        Initialize a BankTransferTransaction object with the specified amount, source account, and destination account.
        The transaction status is set to PENDING by default.

        Args:
            transaction_id (str): The unique identifier for the transaction.
            amount (Decimal): The amount of money to be transferred.
            account (BankAccount): The bank account from which funds will be withdrawn.
            target_account (BankAccount): The bank account to which funds will be deposited.

        Raises:
            ValueError: If the amount is not a positive number.
            ValueError: If the source or target account is None.
        """
        super().__init__(transaction_id, amount, account)
        
        if target_account is None:
            raise ValueError("Target account cannot be None.")
        
        self._target_account: BankAccount = target_account

    @property
    def target_account(self) -> BankAccount:
        """
        Get the target bank account for the transfer.

        Returns:
            BankAccount: The bank account to which funds will be deposited.
        """
        return self._target_account

    @property
    def fees(self) -> Decimal:
        """
        Calculate the transaction fee based on the amount and fee rate.

        Returns:
            Decimal: The calculated transaction fee.
        """
        percentage_fee = self.amount * self.FEE_RATE
        fee = max(self.BASE_FEE, percentage_fee)
        return fee.quantize(Decimal("0.01"))  # Round to 2 decimal places

    def process(self) -> None:
        """
        Process the bank transfer transaction.
        This method deducts the amount and fees from the source account and credits the target account.
        It updates the transaction status to PROCESSED if successful, or FAILED if an error occurs.

        Raises:
            ValueError: If the source account has insufficient funds for the transfer and fees.
        """
        source_active = (self._account.status.name.upper() == "ACTIVE")

        target_active = (self._target_account.status.name.upper() == "ACTIVE")

        sufficient_funds = (self._amount + self.fees) <= self._account.balance
        if not (source_active and target_active and sufficient_funds):
            self._status = TransactionStatus.FAILED
            return

        if self.status == TransactionStatus.PENDING:
            self._account.withdraw(self._amount)
            self._account.withdraw(self.fees)
            self._target_account.deposit(self._amount)
            self._status = TransactionStatus.PROCESSED
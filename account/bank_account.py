from decimal import Decimal
from account.account_status import AccountStatus    
from account.client import Client

class BankAccount: 
    """Represents an account at a financial institution. """
    def __init__(self,
                  account_id: int,
                  balance: Decimal, 
                  owner: Client,
                  status: AccountStatus):
        """Initialize the BankAccount object.

        Args:
            account_id (int): Represents the unique identify of the bank account.
            balance (Decimal): Represents the balance of the bank account.
            owner (Client): Represents the owner of the bank account.
            status (AccountStatus): Represents the status of the bank account.
        """

        if int(account_id) <= 0:
            raise ValueError("accountid must be a positive number.")
        self._account_id = account_id
        self._balance = balance
        self._owner = owner
        self._status = status

    @property
    def account_id(self) -> int:
        """int: Gets the read-only account ID of the bank account."""
        return self._account_id

    @property
    def balance(self) -> Decimal:
        """Decimal: Gets the read-only balance of the bank account."""
        return self._balance

    @property
    def owner(self) -> Client:
        """Client: Gets the read-only owner of the bank account."""
        return self._owner

    @property
    def status(self) -> AccountStatus:
        """AccountStatus: Gets the read-only status of the bank account."""
        return self._status

    def update_balance (self, amount: Decimal) -> None:
        """Updates the balance of the bank account.

        Args:
        amount (Decimal): The amount to update the balance by. Can be positive or negative.
        """
        self._balance += amount

    def deposit(self, amount: Decimal) -> None:
        """Deposits an amount into the bank account.

        Args:
             amount (Decimal): The amount to deposit. Must be positive.

        Raises:
             ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("deposit amount must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: Decimal) -> None:
        """Withdraws an amount from the bank account.

        Args:
             amount (Decimal): The amount to withdraw. Must be positive and less than or equal to the current balance.

        Raises:
              ValueError: If the amount is not positive or exceeds the current balance.
        """
        if amount <= 0:
           raise ValueError("withdrawal amount must be positive.")
        if amount > self._balance:
           raise ValueError("insufficient funds for withdrawal.")
        self.update_balance(-amount)

    def __str__(self) -> str:
        """Returns a string representation of the bank account."""
        return (f"BankAccount(account_id={self._account_id}, "
                f"balance={self._balance}, "
                f"owner={self._owner.name}, "
                f"status={self._status.name})")
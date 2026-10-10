"""
Concrete implementation of a credit card transaction.
This module defines the CreditCardTransaction class, which represents a specific type of transaction that involves processing
"""
__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from decimal import Decimal

import pytest

from account.bank_account import BankAccount
from account.account_status import AccountStatus

from transaction.credit_card_transaction import CreditCardTransaction
from transaction.transaction_status import TransactionStatus


@pytest.fixture

def active_account():
    """
    Fixture providing an active BankAccount with $1000.00.
    """
    return BankAccount(
        account_id=123456,
        balance=Decimal("1000.00"),
        owner=None,
        status=AccountStatus.ACTIVE,
    )
    

class TestInit:
    """Tests for the CreditCardTransaction constructor."""

    def test_blank_transaction_id_raises_value_error(self, active_account):
        """Blank id raises ValueError with the expected message."""
        with pytest.raises(
            ValueError, match="transactionid cannot be blank"
        ):
            CreditCardTransaction(
                "   ",
                Decimal("100.00"),
                active_account,
                "AUG111",
            )

    def test_negative_amount_raises_value_error(self, active_account):
        """Negative amount raises ValueError with the expected message."""
        with pytest.raises(
            ValueError, match="amount must be greater than zero"
        ):
            CreditCardTransaction(
                "CC001",
                Decimal("-5.00"),
                active_account,
                "AUG111",
            )
            
            
    def test_zero_amount_raises_value_error(self, active_account):
        """Zero amount raises ValueError with the expected message."""
        with pytest.raises(
            ValueError, match="amount must be greater than zero"
        ):
            CreditCardTransaction(
                "CC001",
                Decimal("0.00"),
                active_account,
                "AUG111",
            )
            
            
    def test_initialize_new_instance(self, active_account):
        """A new instance is initialized with the correct attributes to Pending."""
        txn = CreditCardTransaction(
            "CC001",
            Decimal("100.00"),
            active_account,
            "AUG111",
        )
        assert txn.transaction_id == "CC001"
        assert txn.amount == Decimal("100.00")
        assert txn.account == active_account
        assert txn.authorization_code == "AUG111"
        assert txn.status == TransactionStatus.PENDING
        
        
class TestFees:
    """Tests for the fees property of CreditCardTransaction."""

    def test_return_two_percent_of_amount(self, active_account):
        """Fees equal to 2% of the transaction amount, rounded to two decimal places."""
        txn = CreditCardTransaction(
            "CC001",
            Decimal("100.00"),
            active_account,
            "AUG111",
        )
        expected_fee = Decimal("2.00")  # 2% of  100.00
        assert txn.fees == expected_fee


class TestProcess:
    """Tests for the CreditCardTransaction.process method when the transaction is successful.""" 
    def test_account_inactive_fails(self):
        """If the account is inactive, the transaction fails."""
        account = BankAccount(
            account_id=123456,      
            balance=Decimal("1000.00"),
            owner=None,
            status=AccountStatus.CLOSED,
        )
        txn = CreditCardTransaction(
            "CC001",
            Decimal("100.00"),
            account,
            "AUG111",
        )
        txn.process()
        assert txn.status == TransactionStatus.FAILED
        
    
def test_insufficient_funds_fails(self,active_account):
        """If the account has insufficient funds, the transaction fails."""
        txn = CreditCardTransaction(
            "CC001",
            Decimal("1000.00"),
            active_account,
            "AUG111",
        )
        txn.process()
        assert txn.status == TransactionStatus.FAILED
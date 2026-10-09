"""
Unit tests for the BankTransfer Transaction class
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from decimal import Decimal
import pytest

from account.bank_account import BankAccount
from transaction.bank_transfer_transaction import BankTransferTransaction
from transaction.transaction_status import TransactionStatus


@pytest.fixture
def source_account():
    """
    Fixture to create a source bank account for testing.
    """
    return BankAccount(
        account_id="123456",
        balance=Decimal("1000.00"),
        owner=None,
        status="ACTIVE",
    )
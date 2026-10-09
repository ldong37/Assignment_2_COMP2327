"""
Unit tests for the BankTransfer Transaction class
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from decimal import Decimal

import pytest

from account.bank_account import BankAccount
from account.account_status import AccountStatus
from transaction.bank_transfer_transaction import BankTransferTransaction
from transaction.transaction_status import TransactionStatus


@pytest.fixture
def source_account():
    """
    Fixture to create a source bank account for testing.
    """
    return BankAccount(
           account_id= 123456,
           balance=Decimal("1000.00"),
           owner=None,
           status=AccountStatus.ACTIVE,
    )


@pytest.fixture
def target_account():
    """
    Fixture providing an active target BankAccount with $0.00.
    """
    return BankAccount(
        account_id=676767,
        balance=Decimal("0.00"),
        owner=None,
        status=AccountStatus.ACTIVE,
    )

class TestInit:
    """Tests for the BankTransferTransaction constructor."""

    def test_blank_transaction_id_raises_value_error(
        self, source_account, target_account
    ):
        """Blank id raises ValueError with the expected message."""
        with pytest.raises(
            ValueError, match="transactionid cannot be blank"
        ):
            BankTransferTransaction(
                "   ",
                Decimal("100.00"),
                source_account,
                target_account,
            )

    def test_negative_amount_raises_value_error(
        self, source_account, target_account
    ):
        """Negative amount raises ValueError with the expected message."""
        with pytest.raises(
            ValueError, match="amount must be greater than zero"
        ):
            BankTransferTransaction(
                "TXN001",
                Decimal("-1.00"),
                source_account,
                target_account,
            )

    def test_zero_amount_raises_value_error(
        self, source_account, target_account
    ):
        """Zero amount raises ValueError with the expected message."""
        with pytest.raises(
            ValueError, match="amount must be greater than zero"
        ):
            BankTransferTransaction(
                "TXN001",
                Decimal("0.00"),
                source_account,
                target_account,
            )

    def test_initialize_new_instance(
        self, source_account, target_account
    ):
        """A new instance stores values and defaults to PENDING."""
        txn = BankTransferTransaction(
            "TXN001",
            Decimal("100.00"),
            source_account,
            target_account,
        )
        assert txn.transaction_id == "TXN001"
        assert txn.amount == Decimal("100.00")
        assert txn.account is source_account
        assert txn.target_account is target_account
        assert txn.status == TransactionStatus.PENDING


class TestFees:
    """Tests for the BankTransferTransaction.fees property."""

    def test_returns_base_fee(
        self, source_account, target_account
    ):
        """A small amount yields the flat base fee of $1.00."""
        txn = BankTransferTransaction(
            "TXN002",
            Decimal("10.00"),
            source_account,
            target_account,
        )
        assert txn.fees == Decimal("1.00")

    def test_returns_percentage_fee(
        self, source_account, target_account
    ):
        """A large amount yields 0.7% of the transaction amount."""
        txn = BankTransferTransaction(
            "TXN003",
            Decimal("1000.00"),
            source_account,
            target_account,
        )
        assert txn.fees == Decimal("7.00")


class TestProcess:
    """Tests for the BankTransferTransaction.process method."""

    def test_source_account_inactive_fails(self, target_account):
        """Inactive source account causes status FAILED."""
        source = BankAccount(
            account_id=123456,
            balance=Decimal("1000.00"),
            owner=None,
            status=AccountStatus.CLOSED,
        )
        txn = BankTransferTransaction(
            "TXN004",
            Decimal("100.00"),
            source,
            target_account,
        )
        txn.process()
        assert txn.status == TransactionStatus.FAILED

    def test_target_account_inactive_fails(self, source_account):
        """Inactive target account causes status FAILED."""
        target = BankAccount(
            account_id=676767,
            balance=Decimal("0.00"),
            owner=None,
            status=AccountStatus.CLOSED,
        )
        txn = BankTransferTransaction(
            "TXN005",
            Decimal("100.00"),
            source_account,
            target,
        )
        txn.process()
        assert txn.status == TransactionStatus.FAILED

    def test_insufficient_funds_fails(
        self, source_account, target_account
    ):
        """Amount + fees exceeding balance causes status FAILED."""
        txn = BankTransferTransaction(
            "TXN006",
            Decimal("1000.00"),
            source_account,
            target_account,
        )
        txn.process()
        assert txn.status == TransactionStatus.FAILED

    def test_successful_transfer(
        self, source_account, target_account
    ):
        """Valid transfer updates both balances and status."""
        txn = BankTransferTransaction(
            "TXN007",
            Decimal("100.00"),
            source_account,
            target_account,
        )
        txn.process()

        assert txn.status == TransactionStatus.PROCESSED
        assert source_account.balance == Decimal("899.00")
        assert target_account.balance == Decimal("100.00")


class TestStr:
    """Tests for the BankTransferTransaction string representation."""

    def test_returns_string_representation(
        self, source_account, target_account
    ):
        """String representation matches the expected format."""
        txn = BankTransferTransaction(
            "98765",
            Decimal("2983.35"),
            source_account,
            target_account,
        )
        expected = (
            "ID: 98765 "
            "STATUS: PENDING "
            "AMOUNT: $2,983.35 "
            "SOURCE ACCT: 123456 "
            "--> TARGET ACCT: 676767"
        )
        assert str(txn) == expected


"""
Unit tests for the account status module.
"""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from transaction.transaction_status import TransactionStatus


def test_enumeration_values_initialized():
    """
    Verify that each TransactionStatus member is initialized with the
    expected integer value.
    """
    assert TransactionStatus.PENDING.value == 1
    assert TransactionStatus.PROCESSED.value == 2
    assert TransactionStatus.FAILED.value == 3


def test_enumeration_member_names():
    """
    Verify that the TransactionStatus members use the expected names.
    """
    assert TransactionStatus.PENDING.name == "PENDING"
    assert TransactionStatus.PROCESSED.name == "PROCESSED"
    assert TransactionStatus.FAILED.name == "FAILED"


def test_enumeration_member_count():
    """
    Verify that the enumeration contains exactly three members.
    """
    assert len(TransactionStatus) == 3

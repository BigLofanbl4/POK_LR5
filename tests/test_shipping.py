import pytest

from shipping import shipping_fee


@pytest.mark.parametrize(
    ("order_total_cents", "pickup", "expected_fee"),
    [
        (0, False, 500),
        (4_999, False, 500),
        (5_000, False, 0),
        (5_001, False, 0),
        (0, True, 0),
    ],
)
def test_shipping_fee(order_total_cents, pickup, expected_fee):
    assert shipping_fee(order_total_cents, pickup) == expected_fee


def test_rejects_negative_order_total():
    with pytest.raises(ValueError, match="cannot be negative"):
        shipping_fee(-1)

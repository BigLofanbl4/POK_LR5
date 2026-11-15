def shipping_fee(order_total_cents, pickup=False):
    if order_total_cents < 0:
        raise ValueError("Order total cannot be negative")

    if pickup:
        return 0

    if order_total_cents >= 5_000:
        return 0

    return 500

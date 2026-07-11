def MaximumDiscount(length: int, price: list[int]) -> int:
    # Max discount is achieved by grouping expensive items together
    price_sorted: list[int] = sorted(price, reverse=True)
    discount: int = 0
    for i in range(length):
        if i % 3 == 2:  # Every third item is free
            discount += price_sorted[i]
    return discount




def SumOfThe(n: int, data: list[int]) -> int:
    # Since it is known, that one element is equal to the sum of all others
    # all we have to do is to sum all elements and divide the sum by 2
    total_sum: int = 0
    for num in data:
        total_sum += num
    return total_sum // 2




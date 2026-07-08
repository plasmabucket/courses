def BigMinus(s1: str, s2: str) -> str:
    # Swap numbers so that s1 would be not smaller than s2
    swap: bool = False  # Do we need to swap the numbers
    if len(s1) < len(s2):
        swap = True
    elif len(s1) == len(s2):
        for i in range(len(s1)):
            if int(s1[i]) > int(s2[i]):
                break
            if int(s1[i]) < int(s2[i]):
                swap = True
                break
    if swap:
        s1, s2 = s2, s1
    # Add additional zeroes to s2 to make numbers the same length
    s2 = "0" * (len(s1) - len(s2)) + s2
    # Subtract digits, starting from the smallest one
    result: list[str] = []
    borrow: bool = False  # Do we borrow from the current digit
    for i in range(len(s1) - 1, -1, -1):
        digit: int = int(s1[i]) - (int(s2[i]) + int(borrow))
        borrow = False
        if digit < 0:
            digit += 10
            borrow = True
        result.insert(0, str(digit))
    # Remove leading zeroes
    while len(result) > 1 and result[0] == "0":
        result.pop(0)
    return "".join(result)




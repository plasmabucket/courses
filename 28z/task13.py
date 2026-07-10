def UFO(n: int, data: list[int], octal: bool) -> list[int]:
    base: int = 16
    if octal:
        base = 8
    result: list[int] = []
    for num in data:
        decoded_num: int = 0
        power: int = 0
        while num > 0:
            decoded_num += (num % 10) * base ** power
            power += 1
            num = num // 10
        result.append(decoded_num)
    return result




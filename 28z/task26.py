def white_walkers(village: str) -> bool:
    symbols: list[str] = ["0", "1", "2", "3", "4", "5",
                                "6", "7", "8", "9", "="]
    data: str = village + "0"  # Add a trailing zero for ease of parsing
    digits: list[int] = [0]  # Stores encountered digits (with leading zero)
    walkers: list[int] = []  # Stores amounts of walkers between digits
    # Parse the string
    walker_count: int = 0
    for char in data:
        if char not in symbols:
            continue
        if char == "=":
            walker_count += 1
            continue
        digits.append(int(char))
        walkers.append(walker_count)
        walker_count = 0
    # Check for validity
    validity: bool = False
    for i in range(len(digits) - 1):
        if digits[i] + digits[i+1] == 10:
            validity = True
        if digits[i] + digits[i+1] == 10 and walkers[i] != 3:
            validity = False
            break
    return validity




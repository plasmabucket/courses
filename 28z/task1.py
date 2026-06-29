def squirrel(n: int) -> int:
    """Calculates the first digit of a factorial."""
    # Calculate the factorial
    result: int = 1
    for i in range(n):
        result *= (i+1)
    # Get it's first digit
    while result >= 10:
        result = result // 10
    return result


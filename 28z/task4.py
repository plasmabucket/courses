def MadMax(N: int, Tele: list[int]) -> list[int]:
    """Prepares correct starting impulse from telemetry data."""
    sorted_tele: list[int] = sorted(Tele)
    result: list[int] = []
    i: int
    for i in range(N // 2):
        result.append(sorted_tele[i])
    for i in range(N // 2 + 1):
        result.append(sorted_tele[N - 1 - i])
    return result




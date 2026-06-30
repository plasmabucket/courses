def odometer(oksana: list[int]) -> int:
    """Calculates traversed distance given an array of values."""
    total_time: int = 0
    total_distance: int = 0
    # Walking through array with step width of 2
    for i in range(0, len(oksana), 2):
        speed: int = oksana[i]
        time: int = oksana[i + 1]
        time_delta: int = time - total_time
        total_distance += speed * time_delta
        total_time = time
    return total_distance




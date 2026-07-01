def ConquestCampaign(N: int, M: int, L: int, battalion: list[int]) -> int:
    """Calculates the amount of days to capture a field.

    For each cell calculates a distance to the nearest dispatch cell.
    The cell, most remote to all dispatch cells, determines the time
    it takes to capture a field.
    """
    max_min_distance: int = -1  # Maximum distance out of minimal ones
    # Iteration over every grid cell
    i: int
    for i in range(N * M):
        # Calculating coordinates of a cell
        n_coord: int = i // M + 1
        m_coord: int = i % M + 1
        min_distance: int = -1  # Minimum distance to a dispatch cell
        # Calculating distances to dispatch cells
        j: int
        for j in range(0, L * 2, 2):
            distance: int = (abs(n_coord - battalion[j])
                             + abs(m_coord - battalion[j + 1]))
            # Finding distance to a closest dispatch cell
            if j == 0 or distance < min_distance:
                min_distance = distance
        # Finding the distance from the dispatch cell
        # to the most remote uncaptured cell
        if i == 0 or min_distance > max_min_distance:
            max_min_distance = min_distance
    # Time to capture a field equals to max_min_distance + 1
    # due to day counting starting from 1
    return max_min_distance + 1




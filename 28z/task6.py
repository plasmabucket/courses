def PatternUnlock(n: int, hits: list[int]) -> str:
    """Generates a password based on a list of number hits."""
    ROOT_2: float = 1.4142135623730951  # Length of a diagonal
    # Dictionary for translating numbers into grid coordinates
    grid: dict[int, tuple[int, int]] = {6: (0, 0), 1: (0, 1), 9: (0, 2),
                                        5: (1, 0), 2: (1, 1), 8: (1, 2),
                                        4: (2, 0), 3: (2, 1), 7: (2, 2)}
    # Translation of hits to a sequence of coordinates
    grid_hits: list[tuple[int, int]]
    grid_hits = [grid[hit] for hit in hits]
    # Go through each pair of coordinates and
    # add length of all line segments
    line_len: float = 0.0  # Stores length of drawn line
    i: int
    for i in range(n - 1):
        # Count a diagonal when both coordinates change
        if (grid_hits[i][0] != grid_hits[i + 1][0] and
                grid_hits[i][1] != grid_hits[i + 1][1]):
            line_len += ROOT_2
        else:
            line_len += 1
    # Generate a password from line length
    password: str = str(round(line_len, 5)).replace(".", "")
    password = password.replace("0", "")
    return password




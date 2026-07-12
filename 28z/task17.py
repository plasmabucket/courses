def LineAnalysis(line: str) -> bool:
    correctness: bool = True
    dot_count: int = 0  # How many dots we counted in the current segment
    dot_count_prev: int = 0  # Number of dots in the previous segment
    first_star: bool = True  # Flag to skip the first star
    first_segment: bool = True  # Flag to treat first segment as a reference
    for char in line:
        # Skip the first star
        if first_star:
            first_star = False
            continue
        # Count the dots in a segment
        if char == ".":
            dot_count += 1
        else:
            # Set the first segment as a reference
            if first_segment:
                dot_count_prev = dot_count
                first_segment = False
            # Check the correctness of a segment
            if dot_count != dot_count_prev:
                correctness = False
                break
            # Update counters
            dot_count_prev = dot_count
            dot_count = 0
    return correctness




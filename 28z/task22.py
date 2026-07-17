def SherlockValidString(string: str) -> bool:
    # Count characters
    frequency: dict[str, int] = {}
    for char in string:
        frequency.setdefault(char, 0)
        frequency[char] += 1
    # Count how many different frequencies we've got
    distribution: dict[int, int] = {}
    for value in frequency.values():
        distribution.setdefault(value, 0)
        distribution[value] += 1
    # Sort frequency counts in descending order
    dist_list: list[tuple[int, int]] = list(
        zip(distribution.values(), distribution.keys()))
    dist_list.sort(reverse=True)
    # How many segments are different from the most frequent one
    delta: int = sum(distribution.values()) - dist_list[0][0]
    # The string is valid...
    validity: bool = (delta == 0 or  # If all segments are the same or
                      delta == 1 and  # If only one segment is different and
                      (dist_list[1][1] == 1 or  # its length is one, or
                       # its length is one more than the most frequent
                       dist_list[1][1] - 1 == dist_list[0][1] or
                       # If there are two segments with frequency of one
                       (dist_list[0][0] == 1 and
                        # And the first is one character longer than the second
                        dist_list[0][1] - 1 == dist_list[1][1])))
    return validity




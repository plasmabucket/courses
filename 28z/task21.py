def BiggerGreater(data: str) -> str:
    position: int = -1  # Index of the first char which would differ
    # Search for the first valid swap target
    traversed_chars: list[str] = []
    for i in range(len(data) - 1, -1, -1):
        traversed_chars.append(data[i])
        for char in traversed_chars:
            if char > data[i]:
                position = i
                break
        if position != -1:
            break
    # Return empty string if the target was not found
    if position == -1:
        return ""
    # Generate the output string
    result_list: list[str] = list(data[0:position])
    traversed_chars.sort()
    least_greater_char: str = ""
    for i in range(len(traversed_chars)):
        if traversed_chars[i] > data[position]:
            least_greater_char = traversed_chars[i]
            break
    result_list.append(least_greater_char)
    traversed_chars.remove(least_greater_char)
    result_list.extend(traversed_chars)
    return "".join(result_list)




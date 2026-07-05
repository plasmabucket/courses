def WordSearch(line_len: int, s: str, search: str) -> list[int]:
    # Convert a string to a list of characters for manipulation on words
    s_list: list[str] = list(s)
    # Split long words into parts to fit into line length
    char_count: int = 0
    for i in range(len(s_list)):
        char_count += 1
        if s_list[i] == " ":
            char_count = 0
        if char_count > line_len:
            # Long words are split into parts by a space
            s_list[i] = "".join([" ", s_list[i]])
            char_count = 1
    # Join the list back to a string
    string: str = "".join(s_list)
    # Split the new string into words
    words: list[str] = string.split()
    # Create a list of lines with words
    lines: list[list[str]] = [[]]
    line_count: int = 0
    line_chars: int = 0
    for word in words:
        # Go to the next line if there is not enough char space
        if line_chars + len(word) > line_len:
            lines.append([])
            line_count += 1
            line_chars = 0
        lines[line_count].append(word)
        line_chars += len(word) + 1  # 1 is for the space between words
    # Determine which lines contain the word we are looking for
    result: list[int] = []
    for line in lines:
        if search in line:
            result.append(1)
        else:
            result.append(0)
    return result




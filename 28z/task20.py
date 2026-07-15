history: list[str] = [""]
current_position: int = 0


def BastShoe(command: str) -> str:
    global history
    global current_position
    arguments: list[str] = command.split(" ", 1)
    operation: str = arguments[0]
    if ((operation == "1" or operation == "2")
            and current_position != len(history) - 1):
        # Reset history if editing after undo
        history = [history[current_position]]
        current_position = 0
    if operation == "1":
        # Add string
        addend: str = arguments[1]
        history.append(history[current_position] + addend)
        current_position += 1
    if operation == "2":
        # Remove characters
        count: int = min(int(arguments[1]), len(history[current_position]))
        new_line: str = history[current_position][0:-count]
        history.append(new_line)
        current_position += 1
    if operation == "3":
        # Return character
        index: int = int(arguments[1])
        character: str = history[current_position][index:index+1]
        return character
    if operation == "4":
        # Undo
        current_position = max(0, current_position - 1)
    if operation == "5":
        # Redo
        current_position = min(len(history) - 1, current_position + 1)

    return history[current_position]




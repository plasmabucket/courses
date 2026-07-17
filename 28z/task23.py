def TreeOfLife(H: int, W: int, N: int, initial_tree: list[str]) -> list[str]:
    # Create a list of integers -- map of branch ages
    tree: list[list[int]] = []
    for i in range(H):
        int_row: list[int] = []
        for j in range(W):
            value: int = 0
            if initial_tree[i][j] == "+":
                value = 1
            int_row.append(value)
        tree.append(int_row)

    # Create a list of booleans -- map of branches to destruct
    destroyed: list[list[bool]] = []
    for i in range(H):
        row_bool: list[bool] = []
        for j in range(W):
            row_bool.append(False)
        destroyed.append(row_bool)

    # Simulation loop
    for year in range(N):
        # Increase the age of every branch
        for i in range(H * W):
            tree[i // W][i % W] += 1
        # Skip branch destruction on "even" years
        if year % 2 == 0:
            continue
        # Raise flags on the map of cells to be destroyed
        for i in range(H * W):
            x_coord: int = i % W
            y_coord: int = i // W
            # Only branches of age 3 and older are destroyed
            if tree[y_coord][x_coord] < 3:
                continue
            # This cell and adjacent cells will be destroyed
            destroyed[y_coord][x_coord] = True
            if x_coord != 0:
                destroyed[y_coord][x_coord - 1] = True
            if x_coord != W - 1:
                destroyed[y_coord][x_coord + 1] = True
            if y_coord != 0:
                destroyed[y_coord - 1][x_coord] = True
            if y_coord != H - 1:
                destroyed[y_coord + 1][x_coord] = True
        # Destroy all cells on which the flag was raised
        for i in range(H * W):
            x_coord = i % W
            y_coord = i // W
            if destroyed[y_coord][x_coord]:
                tree[y_coord][x_coord] = 0
            destroyed[y_coord][x_coord] = False

    # Generate result
    result: list[str] = []
    for i in range(H):
        row: list[str] = []
        for j in range(W):
            char: str = "."
            if tree[i][j] > 0:
                char = "+"
            row.append(char)
        result.append("".join(row))
    return result




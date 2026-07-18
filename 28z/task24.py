def MatrixTurn(data: list[str], M: int, N: int, T: int) -> None:
    # Create a matrix of elements
    matrix: list[list[str]] = []
    for i in range(M):
        matrix.append([])
        for j in range(N):
            matrix[i].append(data[i][j])

    # Create rings
    rings: list[list[str]] = []
    for r in range(min(M, N) // 2):
        new_ring: list[str] = []
        for width in range(r, N - r - 1):
            new_ring.append(matrix[r][width])
        for height in range(r, M - r - 1):
            new_ring.append(matrix[height][N - 1 - r])
        for width in range(N - r - 1, r, -1):
            new_ring.append(matrix[M - 1 - r][width])
        for height in range(M - r - 1, r, -1):
            new_ring.append(matrix[height][r])
        rings.append(new_ring)

    # Rotate rings
    for i in range(T):
        for ring in rings:
            ring.insert(0, ring.pop())

    # Write the result into a matrix
    for r in range(len(rings)):
        index: int = 0
        for width in range(r, N - r - 1):
            matrix[r][width] = rings[r][index]
            index += 1
        for height in range(r, M - r - 1):
            matrix[height][N - 1 - r] = rings[r][index]
            index += 1
        for width in range(N - r - 1, r, -1):
            matrix[M - 1 - r][width] = rings[r][index]
            index += 1
        for height in range(M - r - 1, r, -1):
            matrix[height][r] = rings[r][index]
            index += 1

    # Write the result into original list
    for i in range(len(data)):
        data[i] = "".join(matrix[i])




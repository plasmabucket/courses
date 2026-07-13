def MisterRobot(n: int, data: list[int]) -> bool:
    arr: list[int] = data.copy()
    for i in range(1, n - 1):
        index: int = arr.index(i)
        offset: int = (index + 1 - i) % 2
        arr.pop(index)
        arr.insert(i - 1 + offset, i)
        if offset != 0:
            arr[i-1], arr[i], arr[i+1] = arr[i], arr[i+1], arr[i-1]
    return arr[n-2] < arr[n-1]




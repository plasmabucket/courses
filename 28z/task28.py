def Keymaker(k: int) -> str:
    doors: list[bool] = []
    for i in range(k):
        doors.append(False)
    for i in range(k):
        for j in range(i, k, i + 1):
            doors[j] = not doors[j]
    result: list[str] = []
    for i in range(k):
        if doors[i]:
            result.append("1")
            continue
        result.append("0")
    return "".join(result)




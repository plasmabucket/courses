def Football(F: list[int], N: int) -> bool:
    ind_l: int = -1
    ind_r: int = -1
    for i in range(N - 1):
        if F[i] > F[i + 1]:
            ind_l = i
            break
    for i in range(N - 1, 0, -1):
        if F[i - 1] > F[i]:
            ind_r = i
            break
    if ind_l == -1 or ind_r == -1:
        return False

    f_swap: list[int] = F.copy()
    f_swap[ind_l], f_swap[ind_r] = f_swap[ind_r], f_swap[ind_l]
    is_sorted: bool = True
    for i in range(N - 1):
        if f_swap[i] > f_swap[i + 1]:
            is_sorted = False
            break
    if is_sorted:
        return True

    f_rev: list[int] = F.copy()
    subseq: list[int] = f_rev[ind_l:ind_r + 1]
    subseq.reverse()
    f_rev[ind_l:ind_r + 1] = subseq
    is_sorted = True
    for i in range(N - 1):
        if f_rev[i] > f_rev[i + 1]:
            is_sorted = False
            break
    if is_sorted:
        return True

    return False




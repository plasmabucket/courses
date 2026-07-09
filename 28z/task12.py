def MassVote(n: int, votes: list[int]) -> str:
    # Determine total votes, greatest element and number of greatest elements
    total_votes: int = 0
    lead_count: int = votes[0]
    leaders: int = 0
    for num in votes:
        if num == lead_count:
            leaders += 1
        if num > lead_count:
            lead_count = num
            leaders = 1
        total_votes += num
    # Determine the index of the first greatest element
    leader_index: int = 0
    for i in range(n):
        if votes[i] == lead_count:
            leader_index = i + 1
            break
    # Generate a result string based on the data
    if leaders > 1:
        result: str = "no winner"
    elif lead_count * 2 > total_votes:
        result = "majority winner " + str(leader_index)
    else:
        result = "minority winner " + str(leader_index)
    return result




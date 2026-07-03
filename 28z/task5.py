def SynchronizingTables(n: int, ids: list[int], salary: list[int]) -> list[int]:
    """Returns a list of salaries ordered by corresponding id."""
    # Sort salary and id lists
    ids_sorted: list[int] = sorted(ids)
    salaries_sorted: list[int] = sorted(salary)
    # Create a dictionary of correct id-salary pairs
    table: dict[int, int] = dict(zip(ids_sorted, salaries_sorted))
    # Populate a new salary list using a dictionary of correct pairs
    result: list[int] = [table[key] for key in ids]
    return result




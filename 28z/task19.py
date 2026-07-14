def ShopOLAP(n: int, lines: list[str]) -> list[str]:
    # Deduplicate items
    catalog: dict[str, int] = {}
    for line in lines:
        fields: list[str] = line.split()
        catalog.setdefault(fields[0], 0)
        catalog[fields[0]] += int(fields[1])
    # Sort items
    items: list[str] = list(catalog)
    items.sort()  # Sorts lexicographically
    item_count: int = len(items)
    num_sorted: list[list[str | int]] = []
    for i in range(item_count):
        num_sorted.append([catalog[items[i]], item_count - i, items[i]])
    num_sorted.sort(reverse=True)  # Sorts numerically in descending order
    # Return list of strings
    items = []
    for item in num_sorted:
        items.append(str(item[2]) + " " + str(item[0]))
    return items




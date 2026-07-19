def TransformTransform(data: list[int], n: int) -> bool:
    key_key: int = sum(transform(transform(data)))
    return key_key % 2 == 0


def transform(data: list[int]) -> list[int]:
    data_len: int = len(data)
    result: list[int] = []
    for i in range(data_len):
        for j in range(data_len - i):
            result.append(max(data[j:j + i + 1]))
    return result




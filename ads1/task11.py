class BloomFilter:

    def __init__(self, f_len: int) -> None:
        self.filter_len: int = f_len
        self.bit_array: int = 0  # A regular integer is used as a bit array

    def hash_fun(self, str1: str, random_int: int) -> int:
        result: int = 0
        for c in str1:
            code: int = ord(c)
            result = (result * random_int + code) % self.filter_len
        bit_mask: int = 1 << result
        return bit_mask

    def hash1(self, str1: str) -> int:
        # 17 - random number №1
        return self.hash_fun(str1, 17)

    def hash2(self, str1: str) -> int:
        # 223 - random number №2
        return self.hash_fun(str1, 223)

    def add(self, str1: str) -> None:
        mask: int = self.hash1(str1) | self.hash2(str1)
        self.bit_array = self.bit_array | mask

    def is_value(self, str1: str) -> bool:
        check1: bool = (self.bit_array & self.hash1(str1)) != 0
        check2: bool = (self.bit_array & self.hash2(str1)) != 0
        return check1 and check2




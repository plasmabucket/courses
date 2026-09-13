class NativeCache:

    # 1) Collisions will be resolved by looking for the closest free slot.
    # 2) When we need to drop a key, we choose the one with the least amount
    # of hits.
    #
    # Given these rules, if we allow the table to be completely filled,
    # then the new key will always be inserted in the slot of the least
    # used key. Hashes of these keys are (in principle) uncorrelated,
    # which means that the new key will almost certainly be inserted in a
    # slot which will not match its hash. That means that after many key
    # insertions it can be expected that *all* keys would be in wrong
    # slots, and their positions wouldn't correlate with their respective
    # hashes at all. A search for a key in such table will consistently
    # take O(n) time, which is the same as a search in an unordered array.
    #
    # I couldn't come up with a simple and elegant solution for this problem,
    # so I left it as is.

    def __init__(self, sz: int) -> None:
        self.size: int = sz  # How many slots should be allocated
        self.slots: list[str | None] = [None] * self.size
        self.values: list = [None] * self.size
        self.hits: list[int] = [0] * self.size

    def _hash_fun(self, key: str) -> int:
        random_prime: int = 223
        result: int = 0
        for c in key:
            code: int = ord(c)
            result = (result * random_prime + code) % self.size
        return result

    # Returns the index of an existing key or the index of an empty slot.
    # Returns '-1' if a slot could not be found.
    def _seek_slot(self, key: str) -> int:
        index: int = self._hash_fun(key)
        for i in range(self.size):
            if self.slots[index] is None or self.slots[index] == key:
                return index
            index = (index + 1) % self.size
        return -1

    # Returns an index of the key that was dropped
    def _drop_least_used(self) -> int:
        # Look for a key with the least amount of hits
        index: int = 0
        min_val: int = 0
        first_val: bool = True
        for i in range(self.size):
            if first_val or self.hits[i] < min_val:
                first_val = False
                min_val = self.hits[i]
                index = i
        # Drop the key
        self.slots[index] = None
        self.values[index] = None
        self.hits[index] = 0
        return index

    def put(self, key: str, value) -> None:
        index: int = self._seek_slot(key)
        # Drop an existing key if necessary
        if index == -1:
            index = self._drop_least_used()
        # New key insertion / existing value overwrite
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] += 1  # Value overwrite counts as a hit

    def get(self, key: str):
        index: int = self._seek_slot(key)
        # If the key was not found, return None
        if index == -1 or self.slots[index] is None:
            return None
        self.hits[index] += 1
        return self.values[index]

    # Checks presence of a key in the cache
    def is_key(self, key: str) -> bool:
        index: int = self._seek_slot(key)
        # Presence checks are not counted as hits
        return index != -1 and self.slots[index] == key




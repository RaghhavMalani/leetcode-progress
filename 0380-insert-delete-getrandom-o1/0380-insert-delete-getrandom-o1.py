class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False

        self.store[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False

        index = self.store[val]

        last_value = self.arr[-1]

        self.arr[index] = last_value
        self.store[last_value] = index

        self.arr.pop()

        del self.store[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
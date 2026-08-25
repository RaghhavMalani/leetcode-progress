class SnapshotArray:

    def __init__(self, length: int):
        self.store = [[(0, 0)] for _ in range(length)]
        self.snapid = 0

    def set(self, index: int, val: int) -> None:
        if self.store[index][-1][0] == self.snapid:
            self.store[index][-1] = (self.snapid, val)

        else:
            self.store[index].append((self.snapid, val))

    def snap(self) -> int:
        current = self.snapid
        self.snapid += 1

        return current

    def get(self, index: int, snap_id: int) -> int:
        history = self.store[index]

        left = 0
        right = len(history) - 1

        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if history[mid][0] <= snap_id:

                ans = history[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return ans


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
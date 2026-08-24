class HitCounter:

    def __init__(self):
        self.store = deque()

    def hit(self, timestamp: int) -> None:
        self.store.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        
        while self.store and self.store[0] <= timestamp - 300:
            self.store.popleft()

        return len(self.store)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
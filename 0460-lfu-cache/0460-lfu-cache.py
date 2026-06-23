class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            node.next.prev = node.prev
            node.prev.next = node.next
            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.valMap = {} # key to val 
        self.countMap = collections.defaultdict(int) # key to count
        self.listMap = collections.defaultdict(LinkedList) # count to linkedlist
    
    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[count].pop(key)
        self.listMap[count + 1].pushRight(key)

        if count == self.lfuCnt and self.listMap[count].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
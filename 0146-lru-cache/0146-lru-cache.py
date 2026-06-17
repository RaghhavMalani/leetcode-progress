class Node:
    def __init__(self, key , value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.LRU = Node(0,0) #LEAST RECENTLY USED
        self.MRU = Node(0,0) # MOST RECENTLY USED
        self.LRU.next =  self.MRU
        self.MRU.prev = self.LRU
        self.cache = {}

    def insert(self, node):
        prv = self.MRU.prev
        nxt = self.MRU
        prv.next = node
        nxt.prev = node
        node.prev = prv
        node.next = nxt

    def delete(self,node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv

    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.LRU.next
            self.delete(lru)
            del self.cache[lru.key]
        

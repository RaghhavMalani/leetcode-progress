class Node {
    int val;
    Node prev;
    int key;
    Node next;

    public Node(int key, int val)
    {
        this.val = val;
        this.key = key;
        this.next = null;
        this.prev = null;
    }

    public Node(int key, int val, Node next, Node prev)
    {
        this.val = val;
        this.key = key;
        this.next = next;
        this.prev = prev;
    }
}
class LRUCache {
    int cap;
    Node lru;
    Node mru;
    HashMap <Integer, Node> cache;

    public LRUCache(int capacity) {
        this.cap = capacity;
        lru = new Node(0,0);
        mru = new Node(0,0,null, lru);
        lru.next = mru;
        cache = new HashMap<>();
    }
    private void insert(Node node){
        Node prv = mru.prev;
        prv.next = node;
        mru.prev = node;
        node.next =  mru;
        node.prev = prv;
    }
    
    private void delete(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public int get(int key) {
        if (cache.containsKey(key)){
            Node node = cache.get(key);
            delete(node);
            insert(node);
            return node.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            delete(cache.get(key));
        }
        Node node = new Node(key,value);
        insert(node);
        cache.put(key, node);

        if (cache.size() > cap){
            Node rem = lru.next;
            delete(rem);
            cache.remove(rem.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
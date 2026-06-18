import java.util.*;

class Node {
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
    int cap;
    Node lru;
    Node mru;
    HashMap<Integer, Node> cache;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.cache = new HashMap<>();

        lru = new Node(0, 0);
        mru = new Node(0, 0);

        lru.next = mru;
        mru.prev = lru;
    }

    private void insert(Node node) {
        Node prv = mru.prev;

        prv.next = node;
        node.prev = prv;

        node.next = mru;
        mru.prev = node;
    }

    private void delete(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);

            delete(node);
            insert(node);

            return node.val;
        }

        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node oldNode = cache.get(key);
            delete(oldNode);
        }

        Node node = new Node(key, value);
        insert(node);
        cache.put(key, node);

        if (cache.size() > cap) {
            Node rem = lru.next;

            delete(rem);
            cache.remove(rem.key);
        }
    }
}
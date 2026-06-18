class Node {
public:
    int key;
    int val;
    Node* prev;
    Node* next;

    Node(int key, int val) {
        this->key = key;
        this->val = val;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

class LRUCache {
public:
    int cap;
    Node* lru;
    Node* mru;
    unordered_map<int, Node*> cache;

    LRUCache(int capacity) {
        this->cap = capacity;
        cache = {};

        lru = new Node(0, 0);
        mru = new Node(0, 0);

        lru->next = mru;
        mru->prev = lru;
    }
    
    void insert(Node* node) {
        Node* prv = mru->prev;

        prv->next = node;
        node->prev = prv;

        node->next = mru;
        mru->prev = node;
    }

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    int get(int key) {
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];

            remove(node);
            insert(node);

            return node->val;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if (cache.find(key)!= cache.end()) {
            Node* oldNode = cache[key];
            remove(oldNode);
        }

        Node* node = new Node(key, value);
        insert(node);
        cache[key] = node;

        if (cache.size() > cap) {
            Node* rem = lru->next;

            remove(rem);
            cache.erase(rem->key);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
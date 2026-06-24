class LFUCache {
private:
    class Node {
    public:
        int val;
        Node* prev;
        Node* next;

        Node(int val) {
            this->val = val;
            this->prev = nullptr;
            this->next = nullptr;
        }

        Node(int val, Node* prev, Node* next) {
            this->val = val;
            this->prev = prev;
            this->next = next;
        }
    };

    class LinkedList {
    public:
        Node* left;
        Node* right;
        unordered_map<int, Node*> mp;

        LinkedList() {
            left = new Node(0);
            right = new Node(0);

            left->next = right;
            right->prev = left;
        }

        int length() {
            return mp.size();
        }

        void pushRight(int value) {
            Node* node = new Node(value, right->prev, right);

            right->prev->next = node;
            right->prev = node;

            mp[value] = node;
        }

        void pop(int value) {
            if (mp.find(value) == mp.end()) return;

            Node* node = mp[value];

            node->prev->next = node->next;
            node->next->prev = node->prev;

            mp.erase(value);
        }

        int popLeft() {
            int value = left->next->val;
            pop(value);
            return value;
        }

        void update(int value) {
            pop(value);
            pushRight(value);
        }
    };

    int cap;
    int lfuCnt;

    unordered_map<int, int> valMap;       // key -> value
    unordered_map<int, int> countMap;     // key -> frequency
    unordered_map<int, LinkedList*> listMap; // frequency -> linked list of keys

    LinkedList* getList(int count) {
        if (listMap.find(count) == listMap.end()) {
            listMap[count] = new LinkedList();
        }

        return listMap[count];
    }

    void counter(int key) {
        int count = countMap[key];

        countMap[key] = count + 1;

        getList(count)->pop(key);
        getList(count + 1)->pushRight(key);

        if (count == lfuCnt && getList(count)->length() == 0) {
            lfuCnt++;
        }
    }

public:
    LFUCache(int capacity) {
        this->cap = capacity;
        this->lfuCnt = 0;
    }

    int get(int key) {
        if (valMap.find(key) == valMap.end()) {
            return -1;
        }

        counter(key);
        return valMap[key];
    }

    void put(int key, int value) {
        if (cap == 0) return;

        if (valMap.find(key) == valMap.end() && valMap.size() == cap) {
            int removeKey = getList(lfuCnt)->popLeft();

            valMap.erase(removeKey);
            countMap.erase(removeKey);
        }

        valMap[key] = value;
        counter(key);

        lfuCnt = min(lfuCnt, countMap[key]);
    }
};
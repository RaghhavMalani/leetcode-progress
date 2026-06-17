class Node { 
public:    
    int val;
    Node* next;
    Node* prev;

    Node(int val) {
        this->val = val;
        this->next = nullptr;
        this->prev = nullptr;
    }

    Node(int val, Node* next, Node* prev){
        this->val = val;
        this->next = next;
        this->prev = prev;
    }
};

class MyCircularQueue {
public:
    int space;
    Node* left;
    Node* right;
    Node* node;

    MyCircularQueue(int k) {
        space = k;
        left = new Node(0, nullptr, nullptr);
        right = new Node(0, nullptr, left);
        left->next = right;
    }
    
    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        node = new Node(value, right, right->prev);
        right->prev->next = node;
        right->prev = node;
        space -= 1;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()){
            return false;
        }
        left->next = left->next->next;
        left->next->prev = left;
        space += 1;
        return true;
    }
    
    int Front() {
        if (isEmpty()){
            return -1;
        }
        return left->next->val;
    }
    
    int Rear() {
        if (isEmpty()){
            return -1;
        }
        return right->prev->val;
    }
    
    bool isEmpty() {
        return left->next == right;
    }
    
    bool isFull() {
        return space == 0;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
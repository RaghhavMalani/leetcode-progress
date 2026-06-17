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

    Node(int val, Node* next, Node* prev) {
        this->val = val;
        this->next = next;
        this->prev = prev;
    }
};

class MyCircularQueue {
public:
    int space;
    int capacity;
    Node* left;
    Node* right;

    MyCircularQueue(int k) {
        capacity = k;
        space = k;

        left = new Node(0);
        right = new Node(0);

        left->next = right;
        right->prev = left;
    }
    
    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }

        Node* node = new Node(value, right, right->prev);

        right->prev->next = node;
        right->prev = node;

        space--;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) {
            return false;
        }

        Node* frontNode = left->next;
        Node* secondNode = frontNode->next;

        left->next = secondNode;
        secondNode->prev = left;

        delete frontNode;

        space++;
        return true;
    }
    
    int Front() {
        if (isEmpty()) {
            return -1;
        }

        return left->next->val;
    }
    
    int Rear() {
        if (isEmpty()) {
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
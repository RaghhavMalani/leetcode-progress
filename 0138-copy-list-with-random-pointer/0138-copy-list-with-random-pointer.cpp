/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> oldcopy;
        oldcopy[nullptr] = nullptr;

        Node* curr =  head;
        while (curr != nullptr){
            oldcopy[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;
        while(curr != nullptr){
            Node* copy = oldcopy[curr];
            copy->next = oldcopy[curr->next];
            copy->random = oldcopy[curr->random];
            curr = curr->next;
        }

        return oldcopy[head];
    }
};
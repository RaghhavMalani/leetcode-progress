/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* fast = head->next;
        ListNode* slow = head;

        while (fast and fast->next){
            fast =  fast->next->next;
            slow = slow->next;
        }

        ListNode* second = slow->next;
        slow->next = NULL;
        ListNode* prev =  NULL;

        while (second){
            ListNode* nxt = second->next;
            second->next = prev;
            prev = second;
            second = nxt;
        }

        fast = head;
        second = prev; 
        while (second){
            ListNode* nxt1 = fast->next;
            ListNode* nxt2 = second->next;
            fast->next = second;
            second->next = nxt1;
            fast = nxt1;
            second = nxt2;
        }
        
    }
};
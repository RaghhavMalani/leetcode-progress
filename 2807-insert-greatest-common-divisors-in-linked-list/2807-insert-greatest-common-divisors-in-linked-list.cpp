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
private:
    int dfs(int a, int b){
        while (b > 0){
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr = head;
        while (curr->next != nullptr){
            int v1 = curr->val;
            int v2 = curr->next->val;
            curr->next = new ListNode(dfs(v1,v2),curr->next);
            curr = curr->next->next;
        }
        return head;
    }
};
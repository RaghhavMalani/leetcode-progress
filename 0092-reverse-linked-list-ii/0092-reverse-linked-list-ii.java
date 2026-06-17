/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode current = head;
        ListNode leftprev = dummy;

        for (int i = 0; i < (left - 1);i++){
            current = current.next;
            leftprev = leftprev.next;
        }
        ListNode prev = null;

        for (int i = 0; i < (right - left + 1);i++){
            ListNode temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }

        leftprev.next.next = current;
        leftprev.next = prev;
        return dummy.next;
    }
}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        lp,l = dummy, head

        for _ in range(left - 1):
            lp = lp.next
            l = l.next

        prev = None

        for _ in range(right - left + 1):
            temp = l.next
            l.next = prev
            prev = l
            l = temp

        lp.next.next = l
        lp.next = prev
        return dummy.next
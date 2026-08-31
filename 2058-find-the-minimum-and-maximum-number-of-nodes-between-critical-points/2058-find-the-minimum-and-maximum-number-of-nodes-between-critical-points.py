# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        index = 1

        first = -1
        last = -1

        min_distance = float('inf')

        while curr.next:
            nxt = curr.next

            is_critical = ((curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val) )

            if is_critical:
                if first == -1:
                    first = index
                else:
                    min_distance = min( min_distance,index - last )

                last = index

            prev = curr
            curr = nxt
            index += 1

        if first == last:
            return [-1, -1]

        max_distance = last - first

        return [min_distance, max_distance]
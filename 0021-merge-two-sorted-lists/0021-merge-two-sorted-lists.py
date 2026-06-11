# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = ListNode()
        fres = result
        while list1 != None and list2 != None:
            if (list1.val >= list2.val):
                fres.next = list2
                list2 = list2.next

            else:
                fres.next = list1
                list1 = list1.next

            fres = fres.next
            
        if list1 != None:
            fres.next = list1

        if list2 != None:
            fres.next = list2


        return result.next
        
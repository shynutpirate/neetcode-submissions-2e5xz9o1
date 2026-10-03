# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        pt = res

        p1 = list1
        p2 = list2

        while p1 and p2:

            if p1.val <= p2.val:
                pt.next = p1
                pt = pt.next
                p1 = p1.next
            else:
                pt.next = p2
                pt = pt.next
                p2 = p2.next
        
        if p1:
            pt.next = p1
        if p2:
            pt.next = p2
        
        return res.next
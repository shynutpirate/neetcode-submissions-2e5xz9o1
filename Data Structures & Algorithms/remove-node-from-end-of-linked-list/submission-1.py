# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLength(self, head: ListNode):
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        listLen = self.findLength(head)

        #traverse n elements and remove
        n = listLen - n 

        if n == 0:
            return head.next
        
        prev = None
        curr = head
        for i in range(n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return head


        




        
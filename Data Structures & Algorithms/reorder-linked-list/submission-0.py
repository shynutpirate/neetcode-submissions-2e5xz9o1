# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findMid(self, head: ListNode):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: ListNode):

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find mid
        mid = self.findMid(head)
        list2 = mid.next
        mid.next = None

        #reverse list
        list2 = self.reverseList(list2)

        #merge lists
        list1 = head
        res = ListNode(0)
        curr = res

        while list1 and list2:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

            curr.next = list2
            list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        return None



    
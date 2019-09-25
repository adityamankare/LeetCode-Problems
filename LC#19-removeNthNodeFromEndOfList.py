# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def removeNthFromEnd(self, head, n):
        
        if head == None :
            return None
        if head.next == None and n == 1:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        
        for i in range(n):
            first = first.next
        
        while first.next is not None:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return dummy.next

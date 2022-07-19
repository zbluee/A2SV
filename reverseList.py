#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #iteratively
        prev, curr = None, head
        
        while curr:
            nexxt = curr.next
            curr.next = prev
            prev = curr
            curr = nexxt
            
        return prev
        
        #recursively
        
#         if not head:
#             return None
        
#         newHead = head
        
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
        
#         return newHead
            
        

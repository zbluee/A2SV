#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        length = 0
        
        while itr:
            length += 1
            itr = itr.next
            
        index = length - n
        cur = head
        
        if length == 0:
            return
        
        if length < n :
            return
        
        if length == 1 or index == 0:
            head = head.next
            return head
            
        for _ in range(index - 1):
            cur = cur.next
            
        cur.next = cur.next.next
        
        return head
        

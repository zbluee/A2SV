#https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        itr = head
        while itr.next:
            
            itr = itr.next
            len += 1
        len += 1
        mid = len//2
        
        count = 0
        result = ListNode()
        cur = result
        while head:
            if count >=mid:
                cur.next = ListNode(head.val)
                cur = cur.next
            count += 1 
            head = head.next
        return result.next
                
            
            

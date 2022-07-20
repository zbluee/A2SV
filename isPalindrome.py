#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        con = []
        itr = head
        while itr:
            con.append(itr.val)
            itr = itr.next
            
        return con[::1] == con[::-1]
        

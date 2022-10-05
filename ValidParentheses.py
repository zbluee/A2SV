#Question -> https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in chars.values():
                stack.append(c)
            elif not stack or stack[-1] != chars[c]:
                return False
            else:
                stack.pop()
        return not stack
    
            
            
        

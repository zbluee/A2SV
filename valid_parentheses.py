#Question => https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        characters = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in characters.values():
                stack.append(char)
            elif char in characters.keys():
                if len(stack) == 0 or characters[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
        
        

#Question =>https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if char == ')':
                upto_close = []
                last_element = stack.pop()
                while last_element != '(':
                    upto_close.append(last_element)
                    last_element = stack.pop()
                    
                stack += upto_close
            else:
                stack.append(char)
                
            
        return ''.join([char for char in stack])
        

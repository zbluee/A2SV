#https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:
        
        if not s:
            return 0
        
        stack, current_num, operator = [], 0 , "+"
        operators = {"+", "-", "*", "/"}
        nums = set(str(i) for i in range(10))
        
        for i in range(len(s)):
            char = s[i]
            
            if char in nums:
                current_num = current_num * 10 + int(char)
                
            if char in operators or i == len(s) - 1:
                
                if operator == "+":
                    stack.append(current_num)
                elif operator == "-":
                    stack.append(-current_num)
                elif operator == "*":
                    stack[-1] *= current_num
                elif operator == "/":
                    stack[-1] = int(stack[-1] / current_num)
                current_num = 0
                operator = char
        return sum(stack)
        
        
            
        

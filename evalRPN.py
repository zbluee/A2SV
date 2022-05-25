#Question => https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                num1 , num2= int(stack.pop()), int(stack.pop())
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num2 / num1)
        return int(stack[0])
                    
       
        

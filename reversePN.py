#Questions -> https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    res = num2 + num1
                elif token == '-':
                    res = num2 - num1
                elif token == '*':
                    res = num2 * num1
                else:
                    res = num2 / num1
                stack.append(int(res))
        return stack[0]
        
        
                    
                
        

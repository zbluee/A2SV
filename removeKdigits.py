#Question => https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                k -= 1
                stack.pop()
               
            stack.append(n)
        
        return  '0' if not ''.join(stack[:len(stack)-k]) else str(int(''.join(stack[:len(stack)-k])))

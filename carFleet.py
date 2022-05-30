#Question => https://leetcode.com/problems/car-fleet/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p,s in sorted([(p,s) for p,s in zip(position, speed)], reverse=True):
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
                
        return len(stack)
        
        
        

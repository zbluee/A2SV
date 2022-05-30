#Question => https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, rem = stack.pop()
                answer[index] = i - index
            stack.append((i, temp))
            
        return answer
        

#Question -> https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)
            if min(height[left], height[right]) == height[left]:
                left += 1
            else:
                right -=1
        return maxArea
        

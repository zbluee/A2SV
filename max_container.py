//https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while(left < right):
            width = right - left
            min_height = min(height[left], height[right])
            area = max(area, width * min_height)
            if min_height == height[left]:
                left += 1 
            else: 
                right -= 1
        return area
        
        

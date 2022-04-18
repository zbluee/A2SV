#Question -> https://leetcode.com/problems/sort-colors
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for hole, value in enumerate(nums):
            while(hole > 0 and nums[hole - 1] > value):
                nums[hole] = nums[hole - 1]
                hole -= 1
            nums[hole] = value
        

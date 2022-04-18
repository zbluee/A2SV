#Question -> https://leetcode.com/problems/find-target-indices-after-sorting-array
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_indices  = []
        for hole, value in enumerate(nums):
            while(hole > 0 and nums[hole - 1] > value):
                nums[hole] = nums[hole - 1]
                hole -= 1
            nums[hole] = value

        target_indices = [i for i, v in enumerate(nums) if v == target]
        return target_indices
        

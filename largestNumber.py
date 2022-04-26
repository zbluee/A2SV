#Question -> https://leetcode.com/problems/largest-number/
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums.count(0) == len(nums):
            return ''.join([str(i) for i in nums])[0]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
  
    
        return ''.join([str(i) for i in nums])

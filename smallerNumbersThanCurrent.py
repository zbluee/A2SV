#Question -> https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0 for _ in range(len(nums))]
        for index, i in enumerate(nums):
            count = 0
            for j in nums:
                if i > j:
                    count += 1
                
            result[index] = count
            
        return result

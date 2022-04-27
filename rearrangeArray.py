# Question -> https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i,j = 0, len(nums)-1
        result = []
        
        while i <= j:
            result.append(nums[i])
            i += 1
            
            if i <= j:
                result.append(nums[j])
                j -= 1
            
                
                
        return result
        

#question => https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        result = 0
        counted = []
        
        for num in nums:
            if nums.count(num) > 1 and num not in counted:
                result += nums.count(num) * (nums.count(num) - 1) // 2
                counted.append(num)
        
        return result
        

#Question -> https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map = {}
        for i, j in enumerate(nums):
            if target - j in value_index_map:
                return value_index_map[target - j], i
            value_index_map[j] = i
        
        
        
            
        

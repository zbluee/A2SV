#question => https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operation = 0
        value_Count = {}
        for num in nums:
            if k - num in value_Count and value_Count[k-num] > 0:
                    operation += 1
                    value_Count[k-num] -= 1
                
            else:
                if num in value_Count:
                    value_Count[num] += 1
                else:
                    value_Count[num] = 1
        
        return operation
                
                
        
    

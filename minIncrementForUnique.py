#https://leetcode.com/problems/minimum-increment-to-make-array-unique/
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()
        for i in range(1 , len(nums)):
            previous = nums[i -1]
            current = nums[i]
            if previous >= current:
                moves += previous - current + 1
                nums[i] = previous + 1
        return moves
            
        

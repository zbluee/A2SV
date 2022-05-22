#Question => https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums) - 1
        left = 0
        min_pair_sum = []
        while(right > left):
            min_pair_sum.append((nums[left] + nums[right]))
            left += 1
            right -= 1
        return max(min_pair_sum)
        

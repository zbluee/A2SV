#Question -> https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = 1, 1, [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
        

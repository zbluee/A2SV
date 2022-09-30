#Question -> https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # inorder to remove the duplicates by shifting the pointer once and to solve the 3sum problem using the solution of 2sum II problem with additional loop
        for i,j in enumerate(nums):
            if i == 0 or j != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right :
                    if j + nums[left] + nums[right] == 0:
                        res.append([j, nums[left], nums[right]])
                        # to ignore the duplicates by shifting the pointer
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif j + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return res

#question => https://leetcode.com/problems/arithmetic-subarrays/
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for lindex, rindex in zip(l, r):
            consecutive_difference = []
            sub_nums = sorted(nums[lindex : rindex+1])
            for i in range(len(sub_nums) - 1):
                consecutive_difference.append(sub_nums[i] - sub_nums[i + 1])
            if len(consecutive_difference) == consecutive_difference.count(consecutive_difference[0]):
                answer.append(True)
            else:
                answer.append(False)
        return answer

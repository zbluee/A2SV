#Question ->https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=int, reverse=True)
        return nums[int(k)-1]

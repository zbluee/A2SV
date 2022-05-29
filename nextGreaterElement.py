#question => https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for num in nums1]
        for i, num2 in enumerate(nums2):
            if num2 in nums1:
                for num in nums2[i+1:]:
                    if num2 < num:
                        result[nums1.index(num2)] = num
                        break
            
        return result
           

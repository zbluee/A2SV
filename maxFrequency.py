#question => https://leetcode.com/problems/frequency-of-the-most-frequent-element/
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left, right, most_frequency, total  = 0, 0, 0, 0
        while right < len(nums):
            total += nums[right]
            # to check the valid size of the window , window_size = (right - left + 1)
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            most_frequency = max(most_frequency, right - left + 1)
            right += 1
        return most_frequency
        
        
                
            
        

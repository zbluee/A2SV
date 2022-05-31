#Question=>https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_que = deque([0])
        min_que = deque([0])
        left = 0
        ans = 1
        for right in range(1,len(nums)):
            while max_que and nums[max_que[-1]] < nums[right]:
                max_que.pop()
            max_que.append(right)
            while min_que and nums[min_que[-1]] > nums[right]:
                min_que.pop()
            min_que.append(right)
            
            while max_que and min_que and nums[max_que[0]] - nums[min_que[0]] > limit:
        
                left = min(max_que[0], min_que[0])+1
                if max_que[0] < left:
                    max_que.popleft()
                if min_que[0] < left:
                    min_que.popleft()
            ans = max(ans, right -left + 1)
        return ans
        

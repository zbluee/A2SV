#Question => https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
            
        dq = deque()
        result = float(inf)
        for index,sum_ in enumerate(pre):
            
            while(dq and dq[-1][1] >=sum_):
                dq.pop()
            
            while dq and sum_ - dq[0][1] >= k:
                result = min(index-dq[0][0], result)
                dq.popleft()
                
            dq.append([index,sum_])
        return result if result!= float(inf) else -1 
            
        

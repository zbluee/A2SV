#Question => https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums).most_common(k)
        result = [element[0] for element in c]
        
        return result

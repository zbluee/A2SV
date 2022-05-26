#Question => https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = defaultdict(int)
        count = 0
        for char in order:
            dic[char] = count
            count += 1
            
        return ''.join(sorted(s, key = lambda k:dic[k]))

        
            
        
        
            
            
        
        

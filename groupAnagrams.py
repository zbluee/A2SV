#Questions -> https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(st)
        return result.values()
                
        

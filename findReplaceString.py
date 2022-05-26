#Question =>https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        resulting_s = s
        
        shift = 0
        for index, source, target in sorted(zip(indices, sources, targets)):
            if source == s[index : len(source) + index]:
                index = index + shift
                resulting_s = resulting_s[:index] + target + resulting_s[index+len(source):]
                shift += len(target) - len(source)
                
        return resulting_s

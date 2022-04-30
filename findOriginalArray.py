#Question->https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        changed.sort()
        ch = Counter(changed)
    
        for num in changed:
                if num==0 and ch[num] > 1:
                        ch[num] -= 2
                        original.append(num)

                elif num > 0 and ch[num*2] and ch[num] :
                        ch[num] -= 1
                        ch[num*2] -= 1
                        original.append(num)

        
        return original if len(original) == len(changed) / 2  else []
        

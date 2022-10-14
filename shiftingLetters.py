#Question -> https://leetcode.com/problems/shifting-letters-ii/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * (len(s) + 1)
        res = [0] * len(s)
        for start, end, direction in shifts:
            if direction == 1: #forward
                shift[start] += 1
                shift[end + 1] -= 1
            else:#backward
                shift[start] -= 1
                shift[end + 1] += 1
        for i in range(1, len(s) + 1):
            shift[i] += shift[i - 1]
        
        for i,c in enumerate(s):
            res[i] = chr((ord(c) - ord('a') + shift[i]) % 26 + ord('a'))
        return ''.join(res)

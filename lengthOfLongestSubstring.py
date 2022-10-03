#Question -> https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length = 1
        l, r = 0, 1
        while r < len(s):
            if s[r] not in s[l : r]:
                length = max(length, r - l + 1)
                r += 1
            else:
                l += 1
        return length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        position = 0
        length = 0

        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= position:
                position = dict[s[i]] + 1
            dict[s[i]] = i
            length = max(length, i - position +1)
        return length
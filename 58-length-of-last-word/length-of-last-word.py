class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        while s[last] == " ":
            last -= 1
        
        start = last

        while start >= 0 and s[start] != " ":
            start -= 1
        
        return last - start
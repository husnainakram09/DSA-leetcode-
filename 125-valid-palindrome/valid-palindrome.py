class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(start, end):

            # this is base condition where to stop calling recursion 
            if start >= end:
                return True

            print("start: ", start)
            # skipping all non alphanumeric characters for start 
            while not s[start].isalnum() and start < end:
                start += 1

            print("end: ", end)
            # skipping all non alphanumeric characters for end pointer 
            while end > start and (not s[end].isalnum()):
                end -= 1

            # return and recursive call
            return (s[start].lower() == s[end].lower()) and helper(start + 1, end - 1)

        return helper(0, len(s)-1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if 1 > len(s) or len(s) > 10000:
            return 0
        return len(s.split()[-1])


s = Solution()
print(s.lengthOfLastWord(""))


"""Tests:
1. Runtime: 46 ms, faster than 53.76% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 39.32% of Python3 online submissions for Length of Last Word.

2. Runtime: 44 ms, faster than 59.48% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 39.32% of Python3 online submissions for Length of Last Word.
"""
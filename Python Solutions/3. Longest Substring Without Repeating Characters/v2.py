class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curString = ""
        for char in s:
            if char not in curString:
                curString += char
            else:
                for i in range(len(curString)):
                    if curString[i] == char:
                        curString = curString[i + 1:] + char
                        break
            if len(curString) > maxLength:
                maxLength = len(curString)
        return maxLength


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

"""Tests:
1. Runtime: 53 ms, faster than 98.66% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 13.37% of Python3 online submissions for Longest Substring Without Repeating Characters

2. Runtime: 92 ms, faster than 65.26% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 93.16% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

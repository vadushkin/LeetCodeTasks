class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


s = Solution()
print(s.isPalindrome(123321))

"""Tests:
1. Runtime: 81 ms, faster than 74.65% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 59.40% of Python3 online submissions for Palindrome Number.

2. Runtime: 81 ms, faster than 74.65% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 59.40% of Python3 online submissions for Palindrome Number.
"""

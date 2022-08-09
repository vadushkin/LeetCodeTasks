class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == ''.join(reversed(str(x))):
            return True
        return False


s = Solution()
print(s.isPalindrome(123321))

"""Tests:
1. Runtime: 83 ms, faster than 72.17% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 96.59% of Python3 online submissions for Palindrome Number.

2. Runtime: 80 ms, faster than 75.68% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 96.59% of Python3 online submissions for Palindrome Number.
"""
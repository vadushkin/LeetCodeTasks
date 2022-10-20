class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in charMap:
                if len(stack) == 0 or stack.pop() != charMap[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


s = Solution()
print(s.isValid("{}"))

"""Tests:
1. Runtime: 49 ms, faster than 50.99% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 25.50% of Python3 online submissions for Valid Parentheses.

2. Runtime: 42 ms, faster than 70.15% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 25.50% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, paren),
        return result


def main():
    s = Solution()
    print(s.longestValidParentheses(")()())"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 47 ms, faster than 90.63% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 15.7 MB, less than 9.50% of Python3 online submissions for Longest Valid Parentheses.

2. Runtime: 54 ms, faster than 79.85% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 15.7 MB, less than 7.53% of Python3 online submissions for Longest Valid Parentheses.
"""

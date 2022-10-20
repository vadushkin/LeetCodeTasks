class Solution:
    def longestValidParentheses(self, S: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans


def main():
    s = Solution()
    print(s.longestValidParentheses(")((()))("))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 80 ms, faster than 33.96% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14.6 MB, less than 47.25% of Python3 online submissions for Longest Valid Parentheses.

2. Runtime: 46 ms, faster than 92.20% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14.7 MB, less than 47.25% of Python3 online submissions for Longest Valid Parentheses.
"""

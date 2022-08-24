class Solution:
    def generateParenthesis(self, n: int, is_open=0) -> list[str]:
        if n > 0 <= is_open:
            return ['(' + p for p in self.generateParenthesis(n - 1, is_open + 1)] + \
                   [')' + p for p in self.generateParenthesis(n, is_open - 1)]
        return [')' * is_open] * (not n)


def main():
    s = Solution()
    print(s.generateParenthesis(3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 43 ms, faster than 79.71% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.3 MB, less than 40.19% of Python3 online submissions for Generate Parentheses.

2. Runtime: 71 ms, faster than 19.40% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.1 MB, less than 77.53% of Python3 online submissions for Generate Parentheses.
"""

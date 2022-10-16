from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if j >= len(p):
                return i == len(s)
            if i < len(s) and p[j] in {s[i], '?'}:
                return dp(i + 1, j + 1)
            if p[j] == '*':
                if i < len(s):
                    return dp(i + 1, j) or dp(i, j + 1)
                return dp(i, j + 1)

        return dp(0, 0)


def main():
    s = Solution()
    print(s.isMatch("123", "*"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1443 ms, faster than 30.76% of Python3 online submissions for Wildcard Matching.
Memory Usage: 131.5 MB, less than 11.52% of Python3 online submissions for Wildcard Matching.

2. Runtime: 1546 ms, faster than 26.46% of Python3 online submissions for Wildcard Matching.
Memory Usage: 131.8 MB, less than 9.63% of Python3 online submissions for Wildcard Matching.
"""

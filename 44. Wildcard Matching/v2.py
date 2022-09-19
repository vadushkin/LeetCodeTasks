class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]


def main():
    s = Solution()
    print(s.isMatch("aa", "*"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 404 ms, faster than 84.76% of Python3 online submissions for Wildcard Matching.
Memory Usage: 14.1 MB, less than 84.45% of Python3 online submissions for Wildcard Matching.

2. Runtime: 238 ms, faster than 86.49% of Python3 online submissions for Wildcard Matching.
Memory Usage: 13.9 MB, less than 89.90% of Python3 online submissions for Wildcard Matching.
"""

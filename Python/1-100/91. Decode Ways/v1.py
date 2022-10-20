class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1:i]):
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


def main():
    s = Solution()
    print(s.numDecodings("226"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 75 ms, faster than 9.49% of Python3 online submissions for Decode Ways.
Memory Usage: 13.9 MB, less than 80.35% of Python3 online submissions for Decode Ways.

2. Runtime: 30 ms, faster than 97.47% of Python3 online submissions for Decode Ways.
Memory Usage: 13.9 MB, less than 80.35% of Python3 online submissions for Decode Ways.
"""

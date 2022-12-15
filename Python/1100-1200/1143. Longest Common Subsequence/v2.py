class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if text2[i] == text1[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    elif i - 1 >= 0:
                        dp[i][j] = dp[i - 1][j]
                    elif j - 1 >= 0:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = 0
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.longestCommonSubsequence("hello", "world"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 443 ms Beats 88.14%
   Memory 22.1 MB Beats 67.75%

2. Runtime 452 ms Beats 86.98%
   Memory 22.1 MB Beats 67.75%
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]


def main():
    s = Solution()
    print(s.longestCommonSubsequence("balls", "palls"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 379 ms Beats 96.53%
   Memory 22 MB Beats 81.56%

2. Runtime 395 ms Beats 94.52%
   Memory 22 MB Beats 71.29%
"""

class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]


def main():
    s = Solution()
    print(s.numSquares(12))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 65 ms Beats 88.42%
   Memory 13.7 MB Beats 74.71%

2. Runtime 239 ms Beats 81.66%
   Memory 13.7 MB Beats 63.71%
"""

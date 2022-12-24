class Solution(object):
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5] + [0] * n

        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % 1000000007

        return dp[n - 1]


def main():
    s = Solution()
    print(s.numTilings(6))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 33 ms Beats 95.87%
   Memory 13.9 MB Beats 85.40%
 
2. Runtime 43 ms Beats 80.63% 
   Memory 14 MB Beats 60.63%
"""

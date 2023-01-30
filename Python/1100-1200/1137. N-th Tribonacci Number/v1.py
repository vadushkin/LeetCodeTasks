class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1] + [0] * 35

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]


def main():
    s = Solution()
    print(s.tribonacci(37))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 33 ms Beats 64.92%
   Memory 13.8 MB Beats 54.1%

2. Runtime 29 ms Beats 83.30%
   Memory 13.9 MB Beats 10.24%
"""

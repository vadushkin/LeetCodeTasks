class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True
                    break

        return dp[n]


def main():
    s = Solution()
    print(s.divisorGame(2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 49 ms Beats 54.66%
   Memory 13.7 MB Beats 94.67%

2. Runtime 61 ms Beats 29.83%
   Memory 13.8 MB Beats 94.67%
"""

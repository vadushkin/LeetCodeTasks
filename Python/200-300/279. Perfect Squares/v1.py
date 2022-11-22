from math import inf, sqrt


class Solution:
    dp = [0]

    def numSquares(self, n: int) -> int:
        dp = self.dp
        perfectSq = [pow(i, 2) for i in range(1, int(sqrt(n)) + 1)]

        while len(dp) < n + 1:
            dpI = inf

            for ps in perfectSq:
                if len(dp) < ps:
                    break
                dpI = min(dpI, 1 + dp[-ps])

            dp.append(dpI)

        return dp[n]


def main():
    s = Solution()
    print(s.numSquares(12))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 490 ms Beats 72.77%
   Memory 14 MB Beats 71.48%

2. Runtime 155 ms Beats 87.34%
   Memory 13.9 MB Beats 71.48%
"""

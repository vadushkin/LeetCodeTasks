class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n * k:
            return 0

        if target > n * (1 + k) / 2:
            target = n * (1 + k) - target

        dp = [0] * (target + 1)
        for i in range(1, min(k, target) + 1):
            dp[i] = 1

        for i in range(2, n + 1):
            new_dp = [0] * (target + 1)
            for j in range(i, min(target, i * k) + 1):
                new_dp[j] = new_dp[j - 1] + dp[j - 1]
                if j - 1 > k:
                    new_dp[j] -= dp[j - k - 1]
            dp = new_dp

        return dp[target] % (10 ** 9 + 7)


def main():
    s = Solution()
    print(s.numRollsToTarget(30, 30, 500))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 41 ms, faster than 99.82% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 13.9 MB, less than 98.65% of Python3 online submissions for Number of Dice Rolls With Target Sum.

2. Runtime: 44 ms, faster than 99.82% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 14 MB, less than 89.28% of Python3 online submissions for Number of Dice Rolls With Target Sum.
"""

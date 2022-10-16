class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def dp(n, k, target):
            A = [[0] * (target + 1) for _ in range(n + 1)]
            A[0][0] = 1
            for i in range(1, n + 1):
                for j in range(i, target + 1):
                    for q in range(1, k + 1):
                        if j - q >= 0:
                            A[i][j] += A[i - 1][j - q]
            return A[-1][-1]

        return dp(n, k, target) % (10 ** 9 + 7)


def main():
    s = Solution()
    print(s.numRollsToTarget(30, 30, 500))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1975 ms, faster than 9.29% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 14.5 MB, less than 78.74% of Python3 online submissions for Number of Dice Rolls With Target Sum.

2. Runtime: 2532 ms, faster than 5.05% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 14.6 MB, less than 64.02% of Python3 online submissions for Number of Dice Rolls With Target Sum.
"""

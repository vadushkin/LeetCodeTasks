class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        N = len(jobDifficulty)
        if d > N:
            return -1
        dp = [[float("inf")] * d for _ in range(N)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, N):
            dp[i][0] = max(dp[i - 1][0], jobDifficulty[i])
        for i in range(1, N):
            for j in range(1, min(i + 1, d)):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + max(jobDifficulty[k + 1:i + 1]))
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.minDifficulty([6, 5, 4, 3, 2, 1], 6))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4621 ms, faster than 11.93% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 13.9 MB, less than 93.73% of Python3 online submissions for Minimum Difficulty of a Job Schedule.

2. Runtime: 4591 ms, faster than 12.00% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 14.1 MB, less than 81.63% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
"""

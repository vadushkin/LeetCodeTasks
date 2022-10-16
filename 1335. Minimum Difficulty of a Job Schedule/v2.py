from functools import cache


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)

        @cache
        def dp(i, k):
            if k == d:
                return max(jobDifficulty[i:])
            res = float('inf')
            cur = 0
            for j in range(i, n - d + k):
                cur = max(cur, jobDifficulty[j])
                res = min(res, cur + dp(j + 1, k + 1))
            return res

        return -1 if n < d else dp(0, 1)


def main():
    s = Solution()
    print(s.minDifficulty([5, 3, 2, 1], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1119 ms, faster than 81.63% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 15.5 MB, less than 22.15% of Python3 online submissions for Minimum Difficulty of a Job Schedule.

2. Runtime: 2006 ms, faster than 48.44% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 15.4 MB, less than 22.15% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
"""

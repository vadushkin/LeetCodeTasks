from _bisect import bisect_left


class Solution:
    def jobScheduling(self, s, e, p):
        jobs, n = sorted(zip(s, e, p)), len(s)
        dp = [0] * (n + 1)

        for i in reversed(range(n)):
            k = bisect_left(jobs, jobs[i][1], key=lambda j: j[0])
            dp[i] = max(jobs[i][2] + dp[k], dp[i + 1])

        return dp[0]


def main():
    s = Solution()
    print(s.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 662 ms Beats 87.44%
   Memory 26.3 MB Beats 81.24%

2. Runtime 2054 ms Beats 13.87%
   Memory 26.3 MB Beats 81.24%
"""

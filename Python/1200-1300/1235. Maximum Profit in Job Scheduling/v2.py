from _bisect import bisect_left
from functools import lru_cache


class Solution:
    def jobScheduling(self, s: list[int], e: list[int], p: list[int]) -> int:
        jobs = sorted(zip(s, e, p))

        @lru_cache(None)
        def dfs(i):
            if i >= len(jobs):
                return 0
            k = bisect_left(jobs, jobs[i][1], key=lambda j: j[0])
            return max(dfs(i + 1), jobs[i][2] + dfs(k))

        return dfs(0)


def main():
    s = Solution()
    print(s.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2251 ms Beats 9.3%
   Memory 110.7 MB Beats 5.12%

2. Runtime 751 ms Beats 83.2%
   Memory 110.9 MB Beats 5.12%
"""

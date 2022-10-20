from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:

        cur_sum, h = 0, []
        ans = -float('inf')

        for i, j in sorted(zip(efficiency, speed), reverse=True):
            while len(h) > k - 1:
                cur_sum -= heappop(h)
            heappush(h, j)
            cur_sum += j
            ans = max(ans, cur_sum * i)

        return ans % (10 ** 9 + 7)


def main():
    s = Solution()
    print(s.maxPerformance(5, [5, 4, 3, 0, 6], [5, 4, 3, 3, 4], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 811 ms, faster than 22.79% of Python3 online submissions for Maximum Performance of a Team.
Memory Usage: 29.5 MB, less than 95.36% of Python3 online submissions for Maximum Performance of a Team.

2. Runtime: 918 ms, faster than 10.98% of Python3 online submissions for Maximum Performance of a Team.
Memory Usage: 29.7 MB, less than 83.54% of Python3 online submissions for Maximum Performance of a Team.
"""

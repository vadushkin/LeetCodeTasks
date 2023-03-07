from bisect import bisect_left


class Solution:
    def minimumTime(self, time: list[int], total_trips: int) -> int:
        return bisect_left(range(1, 10 ** 14), total_trips, key=lambda x: sum(x // t for t in time)) + 1


def main():
    s = Solution()
    print(s.minimumTime([1, 2, 3], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 3269 ms Beats 31% 
   Memory 28.5 MB Beats 70.25%

2. Runtime 3269 ms Beats 31% 
   Memory 28.5 MB Beats 70.25%
"""

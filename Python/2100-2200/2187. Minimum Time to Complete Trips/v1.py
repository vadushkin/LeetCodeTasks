class Solution:
    def minimumTime(self, time: list[int], total_trips: int) -> int:
        left, right = 1, total_trips * min(time)

        def f(x):
            return sum(x // t for t in time) >= total_trips

        while left < right:
            mid = (left + right) // 2

            if not f(mid):
                left = mid + 1
            else:
                right = mid

        return left


def main():
    s = Solution()
    print(s.minimumTime([1,2,3],5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1830 ms Beats 95.75% 
   Memory 28.8 MB Beats 5%

2. Runtime 1867 ms Beats 89.75% 
   Memory 28.7 MB Beats 20.50%
"""

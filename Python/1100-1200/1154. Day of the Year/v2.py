class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)):
            days[1] = 29

        return d + sum(days[:m - 1])


def main():
    s = Solution()
    print(s.dayOfYear("2019-01-09"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 65 ms Beats 89.98% 
   Memory 13.9 MB Beats 22.39%

2. Runtime 79 ms Beats 48.19% 
   Memory 14 MB Beats 22.39%
"""

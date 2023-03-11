import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        return (datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10])) - datetime.date(int(date[0:4]), 1,
                                                                                               1)).days + 1


def main():
    s = Solution()
    print(s.dayOfYear("2019-02-10"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 66 ms Beats 89.13% 
   Memory 13.8 MB Beats 62.69%

2. Runtime 79 ms Beats 48.19% 
   Memory 13.8 MB Beats 62.69%
"""

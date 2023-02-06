import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return str(math.sqrt(num)).split('.')[1] == '0'


def main():
    s = Solution()
    print(s.isPerfectSquare(16))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 40 ms Beats 38.92% 
   Memory 13.9 MB Beats 47.29%

2. Runtime 27 ms Beats 91.44% 
   Memory 13.9 MB Beats 7%
"""

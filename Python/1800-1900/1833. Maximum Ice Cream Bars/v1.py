import operator
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        return bisect_right(list(accumulate(sorted(costs), operator.add)), coins)


def main():
    s = Solution()
    print(s.maxIceCream([1, 3, 2, 4, 1], 7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 888 ms Beats 70.16% 
   Memory 28 MB Beats 61.26%

2. Runtime 2021 ms Beats 35.34% 
   Memory 28.1 MB Beats 17.54%
"""

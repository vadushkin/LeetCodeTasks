from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, q) for q in queries]


def main():
    s = Solution()
    print(s.answerQueries([1, 2, 4, 5], [1, 5, 19]))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 105 ms Beats 95.73% 
   Memory 14.3 MB Beats 40.29%
   
2. Runtime 101 ms Beats 97.86%
   Memory 14.1 MB Beats 79.61%
"""

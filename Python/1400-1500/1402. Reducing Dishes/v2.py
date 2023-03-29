from itertools import accumulate


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        return max(accumulate(accumulate([0] + sorted(satisfaction, reverse=True))))


def main():
    s = Solution()
    print(s.maxSatisfaction([-1, -8, 0, 5, -9]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 39 ms Beats 86.39% 
   Memory 13.9 MB Beats 77.85%

2. Runtime 40 ms Beats 81.65% 
   Memory 13.8 MB Beats 77.85%
"""

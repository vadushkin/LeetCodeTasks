from itertools import accumulate


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = list(accumulate([g - c for g, c in zip(gas, cost)], initial=0))
        return diff.index(min(diff)) if diff[-1] >= 0 else -1


def main():
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 705 ms Beats 79.58%
   Memory 22.7 MB Beats 5.38%

2. Runtime 698 ms Beats 82.82%
   Memory 22.7 MB Beats 5.38% 
"""

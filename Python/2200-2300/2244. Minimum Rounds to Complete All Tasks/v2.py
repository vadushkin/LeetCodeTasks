import collections
import math


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        return max(-1, sum(math.ceil(freq / 3) if freq > 1 else float("-infinity")
                           for freq in collections.Counter(tasks).values()))


def main():
    s = Solution()
    print(s.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1046 ms Beats 70.33%
   Memory 28.2 MB Beats 70.66%

2. Runtime 963 ms Beats 95.57%
   Memory 28.3 MB Beats 70.66%
"""

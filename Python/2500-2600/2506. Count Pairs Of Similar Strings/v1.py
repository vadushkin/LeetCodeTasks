from collections import Counter
from functools import reduce
from operator import or_


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        ans = 0
        freq = Counter()

        for word in words:
            mask = reduce(or_, (1 << ord(ch) - 97 for ch in word))
            ans += freq[mask]
            freq[mask] += 1

        return ans


def main():
    s = Solution()
    print(s.similarPairs(["nba", "cba", "dba"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 98 ms Beats 73.57%
   Memory 14 MB Beats 37.21%

2. Runtime 91 ms Beats 76.52% 
   Memory 13.9 MB Beats 70.32%
"""

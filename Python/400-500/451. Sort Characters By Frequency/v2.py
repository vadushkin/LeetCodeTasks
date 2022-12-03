import collections
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        dic = collections.Counter(s)
        freq = []

        for k, v in dic.items():
            heapq.heappush(freq, (-1 * v, k))

        curr = ''

        while freq:
            count, c = heapq.heappop(freq)
            count *= -1
            curr += count * c

        return curr


def main():
    s = Solution()
    print(s.frequencySort("iloveleetcode"))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 59 ms Beats 83.63%
   Memory 15.4 MB Beats 49.59%

2. Runtime 76 ms Beats 69.70%
   Memory 15.2 MB Beats 98.50%
"""

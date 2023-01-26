import collections
from heapq import heappop, heappush
from math import inf


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        f = collections.defaultdict(dict)

        for a, b, p in flights:
            f[a][b] = p

        heap = [(0, src, k + 1)]
        dist = [[inf for _ in range(k + 2)] for _ in range(n)]
        dist[src][k + 1] = 0

        while heap:
            p, i, k = heappop(heap)

            if i == dst:
                return p

            if dist[i][k] < p:
                continue

            if k > 0:
                for j in f[i]:
                    if dist[j][k - 1] > p + f[i][j]:
                        dist[j][k - 1] = p + f[i][j]
                        heappush(heap, (p + f[i][j], j, k - 1))
        return -1


def main():
    s = Solution()
    print(s.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 227 ms Beats 53.81%   
   Memory 15.5 MB Beats 26.71%

2. Runtime 249 ms Beats 47.9%
   Memory 15.3 MB Beats 37.88%
"""

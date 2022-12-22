from functools import cache


class Solution:
    def __init__(self):
        self.G = None

    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        self.G = [[] for _ in range(n)]

        for edge in edges:
            self.G[edge[0]].append(edge[1])
            self.G[edge[1]].append(edge[0])

        ans = []

        for i in range(n):
            ans.append(self.dp(i, -1)[0])

        return ans

    @cache
    def dp(self, p_node, source):
        dist = 0
        cnt = 0

        for n in self.G[p_node]:
            if n == source:
                continue

            n_dist, n_cnt = self.dp(n, p_node)
            dist += n_dist + n_cnt
            cnt += n_cnt

        cnt += 1

        return dist, cnt


def main():
    s = Solution()
    print(s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2254 ms Beats 58.89%
   Memory 175.4 MB Beats 5.55%

2. Runtime 2227 ms Beats 60% 
   Memory 175.3 MB Beats 5.55% 
"""

import collections


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:

        graph = collections.defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        ans = [0] * n

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()

        return ans


def main():
    s = Solution()
    print(s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 1120 ms Beats 80.55% 
   Memory 65.6 MB Beats 42.78%

2. Runtime 1080 ms Beats 82.22% 
   Memory 65.5 MB Beats 43.89%
"""

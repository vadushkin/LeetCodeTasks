from collections import defaultdict


class Solution:
    def minTime(self, _, edges: list[list[int]], has_apple: list[bool]) -> int:
        tree = defaultdict(list)

        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        def dfs(node, par):
            res = 0

            for nei in tree[node]:
                if nei != par:
                    res += dfs(nei, node)

            if res or has_apple[node]:
                return res + 2

            return res

        return max(dfs(0, -1) - 2, 0)


def main():
    s = Solution()
    print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                    [False, False, True, False, True, True, False]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 645 ms Beats 98.72%
   Memory 50.8 MB Beats 78.21%

2. Runtime 689 ms Beats 88.46%
   Memory 50.8 MB Beats 78.21%
"""

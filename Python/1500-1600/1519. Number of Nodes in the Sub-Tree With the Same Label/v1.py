from collections import defaultdict, Counter


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        tree = defaultdict(list)

        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        res = [0] * n

        def dfs(node, par):
            nonlocal res
            count = Counter()

            for nei in tree[node]:
                if nei != par:
                    count += dfs(nei, node)

            count[labels[node]] += 1
            res[node] = count[labels[node]]

            return count

        dfs(0, -1)
        return res


def main():
    s = Solution()
    print(s.countSubTrees(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 3199 ms Beats 69.23%
   Memory 180.5 MB Beats 77.56%

2. Runtime 3163 ms Beats 69.87%
   Memory 180.4 MB Beats 77.56 %
"""

from collections import defaultdict
from math import comb


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)

        tree = defaultdict(list)

        val2_nodes = defaultdict(set)

        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)
            val2_nodes[vals[s]].add(s)
            val2_nodes[vals[e]].add(e)

        res = len(vals)

        for v in sorted(val2_nodes.keys()):
            for node in val2_nodes[v]:
                for nei in tree[node]:
                    if vals[nei] <= v:
                        union(node, nei)

            group_count = defaultdict(int)

            for node in val2_nodes[v]:
                group_count[find(node)] += 1

            for root in group_count.keys():
                res += comb(group_count[root], 2)

        return res


def main():
    s = Solution()
    print(s.numberOfGoodPaths([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 2523 ms Beats 73.48% 
   Memory 36.6 MB Beats 68.62%

2. Runtime 2320 ms Beats 81.99% 
   Memory 36.6 MB Beats 68.62%
"""

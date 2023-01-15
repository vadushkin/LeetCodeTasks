from collections import Counter


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        res = n = len(vals)
        f = list(range(n))

        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v, i, j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            res += ci * cj
            f[fj] = fi
            count[fi] = Counter({v: ci + cj})

        return res


def main():
    s = Solution()
    print(s.numberOfGoodPaths([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 2932 ms Beats 63.16%
   Memory 43.6 MB Beats 42.11%

2. Runtime 2888 ms Beats 63.77%
   Memory 43.6 MB Beats 42.11%
"""

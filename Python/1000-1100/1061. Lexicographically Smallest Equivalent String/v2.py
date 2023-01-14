class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base_str: str) -> str:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x > root_y:
                uf[root_x] = root_y
            else:
                uf[root_y] = root_x

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []

        for c in base_str:
            res.append(find(c))

        return ''.join(res)


def main():
    s = Solution()
    print(s.smallestEquivalentString("parker", "morris", "parser"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 37 ms Beats 96.55% 
   Memory 14 MB Beats 56.90%

2. Runtime 48 ms Beats 70.11%
   Memory 14 MB Beats 56.90%
"""

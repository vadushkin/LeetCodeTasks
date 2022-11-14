class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:

        UF = {}

        def _find(x: int) -> int:
            if x != UF[x]:
                UF[x] = _find(UF[x])

            return UF[x]

        def _union(x: int, y: int) -> None:

            if x not in UF:
                UF[x] = x
            if y not in UF:
                UF[y] = y

            root_x = _find(x)
            root_y = _find(y)

            UF[root_x] = root_y

        max_x = 10 ** 4

        for x, y in stones:
            _union(x, y + max_x)

        return len(stones) - len({_find(n) for n in UF})


def main():
    s = Solution()
    print(s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 440 ms Beats 43.50%
   Memory 14.6 MB Beats 86.65%

2. Runtime 309 ms Beats 76.63%
   Memory 14.7 MB Beats 72.25%
"""

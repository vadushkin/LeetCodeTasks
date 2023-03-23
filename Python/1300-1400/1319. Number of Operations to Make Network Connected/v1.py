class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        hash_map = [set() for _ in range(n)]

        for x, y in connections:
            hash_map[x].add(y)
            hash_map[y].add(x)

        seen = [0] * n

        def dfs(i):
            if seen[i]:
                return 0

            seen[i] = 1

            for j in hash_map[i]:
                dfs(j)

            return 1

        return sum(dfs(index) for index in range(n)) - 1


def main():
    s = Solution()
    print(s.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 496 ms Beats 80.8% 
   Memory 38.7 MB Beats 42.86%

2. Runtime 537 ms Beats 41.26% 
   Memory 38.7 MB Beats 42.86%
"""

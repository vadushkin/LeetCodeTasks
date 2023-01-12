class Solution:
    def dfs(self, node: int, grid: list[list[int]], visited: list[int], fst: list[int], labels: str):
        visited[node] = 1
        lst = [0] * 26
        lst[ord(labels[node]) - 97] = 1

        for i in grid[node]:
            if visited[i] == 1:
                continue

            x = self.dfs(i, grid, visited, fst, labels)

            for j in range(26):
                lst[j] += x[j]

        fst[node] = lst[ord(labels[node]) - 97]

        return lst

    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        grid = [[] for _ in range(n)]

        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)

        visited = [0] * n
        fst = [0] * n

        self.dfs(0, grid, visited, fst, labels)

        return fst


def main():
    s = Solution()
    print(s.countSubTrees(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 2157 ms Beats 91.67%
   Memory 182.5 MB Beats 69.23%

2. Runtime 2058 ms Beats 95.51%
   Memory 182.6 MB Beats 69.23%
"""

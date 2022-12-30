class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []

        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        dfs(0, [0])

        return res


def main():
    s = Solution()
    print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 96 ms Beats 96.38% 
   Memory 15.7 MB Beats 43.50%

2. Runtime 105 ms Beats 82.79%
   Memory 15.6 MB Beats 97.56%
"""

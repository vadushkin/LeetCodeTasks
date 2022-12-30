class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]], cur=0) -> list[list[int]]:
        if cur == len(graph) - 1:
            return [[len(graph) - 1]]
        return [([cur] + path) for i in graph[cur] for path in self.allPathsSourceTarget(graph, i)]


def main():
    s = Solution()
    print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 119 ms Beats 68.25%
   Memory 15.9 MB Beats 22.19%

2. Runtime 125 ms Beats 66.77%
   Memory 15.9 MB Beats 22.19% 
"""

import collections


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True

            if not seen[curr_node]:
                seen[curr_node] = True

                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True

            return False

        return dfs(source)


def main():
    s = Solution()
    print(s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2156 ms Beats 84.42%
   Memory 296.9 MB Beats 29.57%

2. Runtime 5466 ms Beats 8.23%
   Memory 296.8 MB Beats 29.57%
"""

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        def dfs(node: int, node_color: int) -> bool:
            color[node] = node_color

            for neighbor in adj[node]:
                if color[neighbor] == color[node]:
                    return False

                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False

            return True

        adj = [[] for _ in range(n + 1)]

        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)

        for i in range(1, n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True


def main():
    s = Solution()
    print(s.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1158 ms Beats 65.81%
   Memory 21.4 MB Beats 40.31%
 
2. Runtime 1118 ms Beats 66.71%
   Memory 21.7 MB Beats 39.12%
"""

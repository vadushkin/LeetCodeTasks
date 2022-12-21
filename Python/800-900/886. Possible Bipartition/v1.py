from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        def bfs(source: int):
            q = deque([source])
            color[source] = 0

            while q:
                node = q.popleft()

                for neighbor in adj[node]:
                    if color[neighbor] == color[node]:
                        return False

                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)

            return True

        adj = [[] for _ in range(n + 1)]

        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)

        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True


def main():
    s = Solution()
    print(s.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 683 ms Beats 99.17%
   Memory 20.1 MB Beats 80.54%
 
2. Runtime 1903 ms Beats 34.32%
   Memory 20 MB Beats 92.70%
"""

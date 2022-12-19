import collections


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n
        seen[source] = True
        queue = collections.deque([source])

        while queue:
            curr_node = queue.popleft()

            if curr_node == destination:
                return True

            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        return False


def main():
    s = Solution()
    print(s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 4504 ms Beats 35.96%
   Memory 106.4 MB Beats 61.52%

2. Runtime 1671 ms Beats 99.78% 
   Memory 106.4 MB Beats 61.52%
"""

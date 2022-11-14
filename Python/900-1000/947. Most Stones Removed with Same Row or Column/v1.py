from collections import defaultdict, deque


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        graph_x = defaultdict(list)
        graph_y = defaultdict(list)

        for x, y in stones:
            graph_x[x].append(y)
            graph_y[y].append(x)

        connected_component = 0
        visited = set()

        for x, y in stones:

            if (x, y) not in visited:
                q = deque([(x, y)])
                while q:
                    xo, yo = q.popleft()

                    if (xo, yo) not in visited:
                        visited.add((xo, yo))

                        for i_y in graph_x[xo]:
                            q.append((xo, i_y))
                        for i_x in graph_y[yo]:
                            q.append((i_x, yo))

                connected_component += 1

        return len(stones) - connected_component


def main():
    s = Solution()
    print(s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 424 ms Beats 46.6%
   Memory 14.8 MB Beats 48.46%

2. Runtime 302 ms Beats 77.83%
   Memory 14.8 MB Beats 48.46%
"""

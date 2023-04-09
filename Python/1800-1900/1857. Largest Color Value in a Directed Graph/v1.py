class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n, k = len(colors), 26

        in_degrees = [0] * n
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            in_degrees[v] += 1

        zero_in_degree = set(i for i in range(n) if in_degrees[i] == 0)
        counts = [[0] * k for _ in range(n)]

        for i, c in enumerate(colors):
            counts[i][ord(c) - ord('a')] += 1

        max_count, visited = 0, 0

        while zero_in_degree:
            u = zero_in_degree.pop()
            visited += 1

            for v in graph[u]:
                for i in range(k):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))

                in_degrees[v] -= 1

                if in_degrees[v] == 0:
                    zero_in_degree.add(v)

            max_count = max(max_count, max(counts[u]))

        return max_count if visited == n else -1


def main():
    s = Solution()
    print(s.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 3397 ms Beats 11.91% 
   Memory 75.8 MB Beats 98.21%

2. Runtime 3429 ms Beats 11.31% 
   Memory 75.6 MB Beats 99.40%
"""

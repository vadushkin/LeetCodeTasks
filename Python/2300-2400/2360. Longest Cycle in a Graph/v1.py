class Solution:
    def __init__(self):
        self.seen = None
        self.edges = None

        self.stack = []
        self.visiting = {}
        self.max_length = float('-inf')

    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)

        self.edges = edges
        self.seen = [False] * n

        for i in range(n):
            self.dfs(i)

        return self.max_length if self.max_length > 0 else -1

    def dfs(self, node):
        if not self.seen[node]:
            if node in self.visiting:
                self.max_length = max(self.max_length, len(self.stack) - self.visiting[node])

            elif self.edges[node] != -1:
                self.visiting[node] = len(self.stack)
                self.stack.append(node)

                self.dfs(self.edges[node])

                self.stack.pop()
                self.visiting.pop(node)

            self.seen[node] = True


def main():
    s = Solution()
    print(s.longestCycle([3, 3, 4, 2, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1578 ms Beats 32.40% 
   Memory 133.1 MB Beats 56.8%

2. Runtime 1586 ms Beats 31.47% 
   Memory 132.9 MB Beats 56.8%
"""

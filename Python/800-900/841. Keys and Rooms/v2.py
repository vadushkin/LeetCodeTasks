class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        self.dfs(0, visited, rooms)
        return len(visited) == len(rooms)

    def dfs(self, node, visited, rooms):
        if node in visited:
            return

        visited.add(node)

        for nei in rooms[node]:
            self.dfs(nei, visited, rooms)


def main():
    s = Solution()
    print(s.canVisitAllRooms([[1], [2], [3], []]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 106 ms Beats 67.68%
   Memory 14.7 MB Beats 34.29%

2. Runtime 146 ms Beats 44.55%
   Memory 14.8 MB Beats 28.52%
"""

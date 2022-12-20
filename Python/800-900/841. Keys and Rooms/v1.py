class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()

            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)

        return all(seen)


def main():
    s = Solution()
    print(s.canVisitAllRooms([[1], [2], [3], []]))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 157 ms Beats 27.83%
   Memory 14.3 MB Beats 98.97%

2. Runtime 162 ms Beats 20.61%
   Memory 14.5 MB Beats 39.38%
"""

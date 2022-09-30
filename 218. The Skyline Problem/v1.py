from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and buildings[i][0] <= -liveHR[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline


def main():
    s = Solution()
    print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    answer: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 299 ms, faster than 36.17% of Python3 online submissions for The Skyline Problem.
Memory Usage: 18.8 MB, less than 87.25% of Python3 online submissions for The Skyline Problem.

2. Runtime: 291 ms, faster than 38.88% of Python3 online submissions for The Skyline Problem.
Memory Usage: 19 MB, less than 81.45% of Python3 online submissions for The Skyline Problem.
"""

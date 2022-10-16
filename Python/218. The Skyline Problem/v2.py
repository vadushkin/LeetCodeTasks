import heapq


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        x_height_right_tuples = sorted(
            [(L, -H, R) for L, R, H in buildings] + [(R, 0, "empty") for _, R, _ in buildings])
        result, max_heap = [[0, 0]], [(0, float('inf'))]
        for x, negative_height, R in x_height_right_tuples:
            while x >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if negative_height:
                heapq.heappush(max_heap, (negative_height, R))
            curr_max_height = -max_heap[0][0]
            if result[-1][1] != curr_max_height:
                result.append([x, curr_max_height])
        return result[1:]


def main():
    s = Solution()
    print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 277 ms, faster than 43.07% of Python3 online submissions for The Skyline Problem.
Memory Usage: 19.9 MB, less than 43.32% of Python3 online submissions for The Skyline Problem.

2. Runtime: 285 ms, faster than 40.48% of Python3 online submissions for The Skyline Problem.
Memory Usage: 20.3 MB, less than 17.56% of Python3 online submissions for The Skyline Problem.
"""

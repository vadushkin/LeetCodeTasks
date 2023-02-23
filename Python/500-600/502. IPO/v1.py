import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        heap = []
        projects = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(heap, -projects[i][0])
                i += 1

            if heap:
                w -= heapq.heappop(heap)

        return w


def main():
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1075 ms Beats 54.20% 
   Memory 38.7 MB Beats 82.34%

2. Runtime 1065 ms Beats 58.22% 
   Memory 38.8 MB Beats 42.66%
"""

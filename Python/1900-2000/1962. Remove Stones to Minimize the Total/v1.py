import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))

        return -sum(heap)


def main():
    s = Solution()
    print(s.minStoneSum([5, 4, 9], 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1964 ms Beats 78.73%
   Memory 28.6 MB Beats 67.75%

2. Runtime 1798 ms Beats 93.83% 
   Memory 28.7 MB Beats 44.43%
"""

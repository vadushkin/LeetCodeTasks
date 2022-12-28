import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-a for a in piles]
        heapq.heapify(piles)

        for _ in range(k):
            heapq.heapreplace(piles, piles[0] // 2)

        return -sum(piles)


def main():
    s = Solution()
    print(s.minStoneSum([5, 4, 9], 2))


if __name__ == "__main__":
    main()

""""Tests:
1. Runtime 1671 ms Beats 98.80%
   Memory 28.9 MB Beats 26.24%

2. Runtime 1584 ms Beats 100%
   Memory 29.1 MB Beats 9.61%
"""

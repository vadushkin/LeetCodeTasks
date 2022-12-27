class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        count = sorted(c - r for c, r in zip(capacity, rocks))[::-1]
        while count and additionalRocks and count[-1] <= additionalRocks:
            additionalRocks -= count.pop()
        return len(rocks) - len(count)


def main():
    s = Solution()
    print(s.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 952 ms Beats 90.46%
   Memory 22 MB Beats 87.83%

2. Runtime 947 ms Beats 92.11%
   Memory 22.1 MB Beats 69.41%
"""

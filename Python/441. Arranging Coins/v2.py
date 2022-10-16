class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)


def main():
    s = Solution()
    for i in range(1, 16):
        print(s.arrangeCoins(i))
        print()


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 77.41% of Python3 online submissions for Arranging Coins.
Memory Usage: 13.9 MB, less than 12.62% of Python3 online submissions for Arranging Coins.

2. Runtime: 64 ms, faster than 69.97% of Python3 online submissions for Arranging Coins.
Memory Usage: 14 MB, less than 12.62% of Python3 online submissions for Arranging Coins.
"""

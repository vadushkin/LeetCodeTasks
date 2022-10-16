class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right


def main():
    s = Solution()
    print(s.arrangeCoins(8))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 75.18% of Python3 online submissions for Arranging Coins.
Memory Usage: 13.9 MB, less than 12.62% of Python3 online submissions for Arranging Coins.

2. Runtime: 73 ms, faster than 58.15% of Python3 online submissions for Arranging Coins.
Memory Usage: 13.9 MB, less than 12.62% of Python3 online submissions for Arranging Coins.
"""

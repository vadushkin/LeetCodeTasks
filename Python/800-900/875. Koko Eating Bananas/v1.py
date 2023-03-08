class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            middle = (left + right) // 2

            if sum((pile + middle - 1) // middle for pile in piles) > h:
                left = middle + 1
            else:
                right = middle

        return left


def main():
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11], 8))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 430 ms Beats 86.49% 
   Memory 15.5 MB Beats 62.98%

2. Runtime 430 ms Beats 86.49% 
   Memory 15.5 MB Beats 16.17%
"""

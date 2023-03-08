from bisect import bisect_left


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        return bisect_left(range(1, 1_000_000_000), -h, key=lambda k: -sum((v + k - 1) // k for v in piles)) + 1


def main():
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11], 8))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 426 ms Beats 87.10% 
   Memory 15.4 MB Beats 62.98%
   
2. Runtime 434 ms Beats 85.67% 
   Memory 15.5 MB Beats 62.98%
"""

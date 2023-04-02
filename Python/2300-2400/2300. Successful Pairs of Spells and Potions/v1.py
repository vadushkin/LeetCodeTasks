from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + spell - 1) // spell) for spell in spells]


def main():
    s = Solution()
    print(s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1209 ms Beats 92.92% 
   Memory 37.7 MB Beats 19.55%

2. Runtime 1209 ms Beats 92.92% 
   Memory 37.7 MB Beats 19.55%
"""

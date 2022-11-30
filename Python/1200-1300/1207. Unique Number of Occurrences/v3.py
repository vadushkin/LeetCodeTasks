from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        return len(c := Counter(arr)) == len(set(c.values()))


def main():
    s = Solution()
    print(s.uniqueOccurrences([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 75 ms Beats 33.33% 
   Memory 13.9 MB Beats 97.26%

2. Runtime 84 ms Beats 12.15%
   Memory 14 MB Beats 34.11%
"""

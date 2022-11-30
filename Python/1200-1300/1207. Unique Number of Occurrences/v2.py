from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        return len(set(arr)) == len(set(Counter(arr).values()))


def main():
    s = Solution()
    print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 77 ms Beats 27.16%
   Memory 14 MB Beats 72.74%

2. Runtime 49 ms Beats 78.69%
   Memory 14 MB Beats 34.11%
"""

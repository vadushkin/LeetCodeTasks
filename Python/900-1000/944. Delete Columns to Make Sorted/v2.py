class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*strs))


def main():
    s = Solution()
    print(s.minDeletionSize(['abc', 'bcd', 'def']))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 286 ms Beats 55.37% 
   Memory 14.5 MB Beats 93.5%

2. Runtime 338 ms Beats 49.90%
   Memory 14.6 MB Beats 61.89%
"""

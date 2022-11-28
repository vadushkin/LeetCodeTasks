from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(combinations(range(1, n + 1), k))


def main():
    s = Solution()
    print(s.combine(4, 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 210 ms Beats 84.72% 
   Memory 15.9 MB Beats 52.58%

2. Runtime 219 ms Beats 83.60%
   Memory 15.9 MB Beats 85.82%
"""

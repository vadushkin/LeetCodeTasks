class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(list(map(lambda x: x * x, nums)))


def main():
    s = Solution()
    print(s.sortedSquares([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 206 ms Beats 96.49% 
   Memory 16.2 MB Beats 43.38%

2. Runtime 213 ms Beats 91.91% 
   Memory 16.4 MB Beats 13.80%
"""

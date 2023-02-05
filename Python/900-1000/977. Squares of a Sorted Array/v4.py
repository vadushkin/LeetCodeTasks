class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(i ** 2 for i in nums)


def main():
    s = Solution()
    print(s.sortedSquares([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 227 ms Beats 75.64% 
   Memory 16.3 MB Beats 43.38%

2. Runtime 205 ms Beats 96.99% 
   Memory 16.3 MB Beats 43.38%
"""

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        return nums


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 684 ms Beats 93.16% 
   Memory 21.1 MB Beats 99.38%

2. Runtime 650 ms Beats 96.73% 
   Memory 21.1 MB Beats 99.82%
"""

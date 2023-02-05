from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return bisect_left(nums, target)


def main():
    s = Solution()
    print(s.searchInsert([1, 2, 3, 4, 5, 6, 8], 100))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 54 ms Beats 62.24% 
   Memory 14.7 MB Beats 33.39%
   
2. Runtime 45 ms Beats 95.13% 
   Memory 14.6 MB Beats 98.64%
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)


def main():
    s = Solution()
    print(s.searchInsert([1, 2, 3, 4, 5, 6, 8], 100))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 58 ms Beats 42.6% 
   Memory 14.8 MB Beats 33.39%

2. Runtime 49 ms Beats 85% 
   Memory 14.7 MB Beats 33.39%
"""

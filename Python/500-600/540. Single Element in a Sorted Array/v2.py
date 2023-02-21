class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]


def main():
    s = Solution()
    print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 176 ms Beats 75.41% 
   Memory 23.6 MB Beats 86.81%
   

2. Runtime 161 ms Beats 98.38% 
   Memory 23.6 MB Beats 86.81%
"""

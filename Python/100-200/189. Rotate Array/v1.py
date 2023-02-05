class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]


def main():
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 207 ms Beats 96.53% 
   Memory 25.4 MB Beats 76.82%

2. Runtime 213 ms Beats 92.29% 
   Memory 25.5 MB Beats 28.80%
"""

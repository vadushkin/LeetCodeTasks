class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        i, j = 0, 1
        for cnt in range(len(nums)):
            i, j = j, max(k + nums[k] + 1 for k in range(i, j))

            if j >= len(nums):
                return cnt + 1


def main():
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 117 ms Beats 98.94% 
   Memory 15 MB Beats 89.52%

2. Runtime 133 ms Beats 76.8% 
   Memory 15.1 MB Beats 54.98%
"""

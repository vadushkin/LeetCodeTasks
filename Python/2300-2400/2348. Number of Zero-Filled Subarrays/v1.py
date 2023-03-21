class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total_zero_sub_arrays = current_zero_sub_arrays = 0

        for num in nums:
            if num == 0:
                current_zero_sub_arrays += 1
                total_zero_sub_arrays += current_zero_sub_arrays
            else:
                current_zero_sub_arrays = 0

        return total_zero_sub_arrays


def main():
    s = Solution()
    print(s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1081 ms Beats 81.27% 
   Memory 24.5 MB Beats 78.9%

2. Runtime 1042 ms Beats 96.47% 
   Memory 24.7 MB Beats 7.77%
"""

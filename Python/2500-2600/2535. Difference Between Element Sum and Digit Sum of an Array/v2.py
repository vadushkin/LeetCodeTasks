class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digits_sum = 0

        for n in nums:
            while n > 0:
                digits_sum += n % 10
                n //= 10

        return sum(nums) - digits_sum


def main():
    s = Solution()
    print(s.differenceOfSum([1, 15, 6, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 121 ms Beats 96.4%
   Memory 14.1 MB Beats 52.47%

2. Runtime 127 ms Beats 88.49%
   Memory 14.2 MB Beats 17.2%
"""

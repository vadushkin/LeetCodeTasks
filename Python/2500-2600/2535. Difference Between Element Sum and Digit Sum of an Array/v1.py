class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        summary = 0

        for i in nums:
            if len(str(i)) > 1:
                for j in str(i):
                    summary += int(j)
            else:
                summary += i

        return sum(nums) - summary


def main():
    s = Solution()
    print(s.differenceOfSum([1, 15, 6, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 157 ms Beats 34.21%
   Memory 14.2 MB Beats 52.47%

2. Runtime 158 ms Beats 32.28%
   Memory 14.1 MB Beats 90.57%
"""

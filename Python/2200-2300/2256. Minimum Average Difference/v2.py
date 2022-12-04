class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n, total = len(nums), sum(nums)
        l_sum = 0
        result = (10 ** 5 + 1, 10 ** 5 + 1)

        for index, val in enumerate(nums):
            l_sum += val
            right_sum = total - l_sum

            if index != (n - 1):
                diff = abs((l_sum // (index + 1)) - (right_sum // (n - (index + 1))))
            else:
                diff = abs((l_sum // (index + 1)))

            if diff < result[1]:
                result = (index, diff)

        return result[0]


def main():
    s = Solution()
    print(s.minimumAverageDifference([3, 1, 2, 3, 41, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1565 ms Beats 75.64%
   Memory 25 MB Beats 56.92%

2. Runtime 2658 ms Beats 38.80%
   Memory 25 MB Beats 56.92% 
"""

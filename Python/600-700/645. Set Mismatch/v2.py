class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s = n * (n + 1) // 2

        miss = s - sum(set(nums))

        duplicate = sum(nums) + miss - s

        return [duplicate, miss]


def main():
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 181 ms, faster than 99.89% of Python3 online submissions for Set Mismatch.
Memory Usage: 15.8 MB, less than 41.20% of Python3 online submissions for Set Mismatch.

2. Runtime: 486 ms, faster than 38.23% of Python3 online submissions for Set Mismatch.
Memory Usage: 16 MB, less than 23.96% of Python3 online submissions for Set Mismatch.
"""

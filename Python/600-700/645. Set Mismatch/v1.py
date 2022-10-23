class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]


def main():
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 254 ms, faster than 80.88% of Python3 online submissions for Set Mismatch.
Memory Usage: 15.9 MB, less than 41.20% of Python3 online submissions for Set Mismatch.

2. Runtime: 202 ms, faster than 94.56% of Python3 online submissions for Set Mismatch.
Memory Usage: 16 MB, less than 23.96% of Python3 online submissions for Set Mismatch.
"""

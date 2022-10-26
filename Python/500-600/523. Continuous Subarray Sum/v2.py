class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        d = {0: -1}
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]

            if k != 0:
                sums %= k
            if sums in d:
                if i - d[sums] > 1:
                    return True
            else:
                d[sums] = i

        return False


def main():
    s = Solution()
    print(s.checkSubarraySum([1, 2, 3], 6))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2631 ms, faster than 20.45% of Python3 online submissions for Continuous Subarray Sum.
Memory Usage: 33.1 MB, less than 73.31% of Python3 online submissions for Continuous Subarray Sum.

2. Runtime: 1551 ms, faster than 71.57% of Python3 online submissions for Continuous Subarray Sum.
Memory Usage: 33.2 MB, less than 73.31% of Python3 online submissions for Continuous Subarray Sum.
"""

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        if k == 0:
            return False

        hash_map = {0: 0}
        s = 0

        for i in range(len(nums)):
            s += nums[i]

            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True

        return False


def main():
    s = Solution()
    print(s.checkSubarraySum([23, 2, 6, 4, 7], 13))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2694 ms, faster than 16.00% of Python3 online submissions for Continuous Subarray Sum.
Memory Usage: 33.1 MB, less than 73.31% of Python3 online submissions for Continuous Subarray Sum.

2. Runtime: 2999 ms, faster than 5.14% of Python3 online submissions for Continuous Subarray Sum.
Memory Usage: 33.3 MB, less than 24.01% of Python3 online submissions for Continuous Subarray Sum.
"""

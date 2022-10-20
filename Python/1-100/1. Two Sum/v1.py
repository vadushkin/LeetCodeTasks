class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) > 10000 or len(nums) < 2 or target > 100000000 or target < -100000000:
            return
        for h, i in enumerate(nums):
            for k, j in enumerate(nums):
                if i > 100000000 or i < -100000000:
                    return
                if h == k:
                    continue
                if i + j == target:
                    return [h, k]


def main():
    s = Solution()
    print(s.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 10))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime: 7509 ms, faster than 5.43% of Python online submissions for Two Sum.
Memory Usage: 14 MB, less than 94.80% of Python online submissions for Two Sum.

2. Runtime: 5100 ms, faster than 14.14% of Python online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 86.61% of Python online submissions for Two Sum.

3. Runtime: 7905 ms, faster than 5.00% of Python online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 86.61% of Python online submissions for Two Sum.
"""

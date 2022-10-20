from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if sorted(list(Counter(nums).values()))[-1] != 1:
            return Counter(nums).most_common()[0][0]
        return False


def main():
    s = Solution()
    print(s.majorityElement([6, 5, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 171 ms, faster than 95.01% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 86.45% of Python3 online submissions for Majority Element.

2. Runtime: 268 ms, faster than 46.86% of Python3 online submissions for Majority Element.
Memory Usage: 15.6 MB, less than 34.89% of Python3 online submissions for Majority Element.
"""

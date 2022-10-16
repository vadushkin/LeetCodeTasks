class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) // 2]


def main():
    s = Solution()
    print(s.majorityElement([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 205 ms, faster than 76.16% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 86.45% of Python3 online submissions for Majority Element.

2. Runtime: 325 ms, faster than 18.50% of Python3 online submissions for Majority Element.
Memory Usage: 15.4 MB, less than 86.45% of Python3 online submissions for Majority Element.
"""

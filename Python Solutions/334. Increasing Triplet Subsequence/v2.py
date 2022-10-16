class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        num1, num2 = nums[0], float('inf')
        global_min = nums[0]

        for cur in nums[1:]:
            if num2 < cur:
                return True
            if cur < global_min:
                global_min = cur
            elif global_min < cur < num2:
                num1, num2 = global_min, cur
            elif num1 < cur < num2:
                num2 = cur

        return False


def main():
    s = Solution()
    print(s.increasingTriplet([2, 3, 4, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 875 ms, faster than 66.40% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 24.7 MB, less than 48.78% of Python3 online submissions for Increasing Triplet Subsequence.

2. Runtime: 1572 ms, faster than 17.69% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 24.7 MB, less than 18.64% of Python3 online submissions for Increasing Triplet Subsequence.
"""

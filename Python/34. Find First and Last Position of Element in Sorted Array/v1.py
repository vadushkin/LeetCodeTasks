class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        try:
            first = nums.index(target)
        except:
            return [-1, -1]
        last = first
        for i in range(first, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                return [first, last]
            last = i + 1
        return [first, last]


def main():
    s = Solution()
    print(s.searchRange([1], 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 156 ms, faster than 28.68% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.
Memory Usage: 15.5 MB, less than 9.42% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.

2. Runtime: 157 ms, faster than 27.71% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.
Memory Usage: 15.1 MB,less than 99.77% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.
"""

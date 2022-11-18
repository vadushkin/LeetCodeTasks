class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i:]) == sum(nums[i + 1::]):
                return i

        return -1


def main():
    s = Solution()
    print(s.findMiddleIndex([1, -1, 4]))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 99 ms Beats 8.97%
   Memory 13.9 MB Beats 15.23%

2. Runtime 92 ms Beats 20.71%
   Memory 13.8 MB Beats 61.23%
"""

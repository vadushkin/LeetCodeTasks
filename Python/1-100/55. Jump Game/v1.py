class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i

        return not goal


def main():
    s = Solution()
    print(s.canJump([1, 4, 3, 2, 1, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 491 ms Beats 91.4% 
   Memory 15.2 MB Beats 82.53%

2. Runtime 480 ms Beats 94.87%
   Memory 15.3 MB Beats 49.64% 
"""

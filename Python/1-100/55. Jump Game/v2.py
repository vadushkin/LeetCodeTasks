class Solution:
    def canJump(self, nums: list[int]) -> bool:
        curr = nums[0]

        for i in range(1, len(nums)):
            if curr == 0:
                return False

            curr -= 1
            curr = max(curr, nums[i])

        return True


def main():
    s = Solution()
    print(s.canJump([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 521 ms Beats 83.43%
   Memory 15.2 MB Beats 82.53%
   
2. Runtime 544 ms Beats 78.29%
   Memory 15.1 MB Beats 82.53%
"""

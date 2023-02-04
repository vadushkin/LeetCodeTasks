from bisect import bisect_left


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return (lambda x: x if nums[x] == target else -1)(bisect_left(nums, target, 0, len(nums) - 1))


def main():
    s = Solution()
    print(s.search([1, 2, 3, 3, 5], 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 269 ms Beats 32.22% 
   Memory 15.4 MB Beats 97.31%
   
2. Runtime 238 ms Beats 92.8% 
   Memory 15.3 MB Beats 97.31%
"""

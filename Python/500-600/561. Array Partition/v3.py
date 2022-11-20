class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])


def main():
    s = Solution()
    print(s.arrayPairSum([1, 4, 2, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 272 ms Beats 97.76% 
   Memory 16.7 MB Beats 56.64%

2. Runtime 747 ms Beats 18.8%
   Memory 16.8 MB Beats 56.64%
"""

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        return int((sum(nums) - sum(set(nums))) // (len(nums) // 2 - 1))


def main():
    s = Solution()
    print(s.repeatedNTimes([1, 2, 3, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 213 ms Beats 83.22%
   Memory 16.1 MB Beats 6.75%

2. Runtime 211 ms Beats 85.66%
   Memory 16.2 MB Beats 6.75%
"""

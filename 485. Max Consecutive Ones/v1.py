class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        return len(max(''.join([str(i) for i in nums]).split('0')))


def main():
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 795 ms, faster than 15.95% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.9 MB, less than 6.52% of Python3 online submissions for Max Consecutive Ones.

2. Runtime: 704 ms, faster than 26.04% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 15 MB, less than 6.52% of Python3 online submissions for Max Consecutive Ones.
"""

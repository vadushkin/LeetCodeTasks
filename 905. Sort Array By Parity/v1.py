class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: x % 2 != 0)


def main():
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 73 ms, faster than 99.31% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 96.46% of Python3 online submissions for Sort Array By Parity.

2. Runtime: 164 ms, faster than 15.00% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 60.42% of Python3 online submissions for Sort Array By Parity.
"""

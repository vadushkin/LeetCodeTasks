class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0


def main():
    s = Solution()
    print(s.addDigits(19))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 35 ms, faster than 91.38% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 54.15% of Python3 online submissions for Add Digits.

2. Runtime: 36 ms, faster than 89.50% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 95.48% of Python3 online submissions for Add Digits.
"""

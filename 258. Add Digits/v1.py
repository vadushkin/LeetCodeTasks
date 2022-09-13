class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum([int(n) for n in str(num)])
        return num


def main():
    s = Solution()
    print(s.addDigits(654))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 41.75% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 95.48% of Python3 online submissions for Add Digits.

2. Runtime: 39 ms, faster than 83.41% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 54.15% of Python3 online submissions for Add Digits.
"""

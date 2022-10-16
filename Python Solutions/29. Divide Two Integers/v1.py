class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend == -2147483648 and divisor == 1:
            return -2147483648
        return int(dividend / divisor)


def main():
    s = Solution()
    print(s.divide(100, 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 41 ms, faster than 80.72% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.9 MB, less than 77.19% of Python3 online submissions for Divide Two Integers.

2. Runtime: 37 ms, faster than 89.56% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.9 MB, less than 77.19% of Python3 online submissions for Divide Two Integers.
"""

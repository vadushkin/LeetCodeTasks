class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


def main():
    s = Solution()
    print(s.divide(-2147483648, -1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 38.94% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.9 MB, less than 77.19% of Python3 online submissions for Divide Two Integers.

2. Runtime: 63 ms, faster than 27.13% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.9 MB, less than 27.70% of Python3 online submissions for Divide Two Integers.
"""

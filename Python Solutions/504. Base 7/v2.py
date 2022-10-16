import math


class Solution:
    def convertToBase7(self, num: int) -> str:
        fn = lambda n: fn(n // 7) * 10 + n % 7 if n else 0
        return str(int(math.copysign(fn(abs(num)), num)))


def main():
    s = Solution()
    print(s.convertToBase7(100))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 74 ms, faster than 6.16% of Python3 online submissions for Base 7.
Memory Usage: 13.8 MB, less than 97.24% of Python3 online submissions for Base 7.

2. Runtime: 64 ms, faster than 21.34% of Python3 online submissions for Base 7.
Memory Usage: 13.8 MB, less than 59.61% of Python3 online submissions for Base 7.
"""

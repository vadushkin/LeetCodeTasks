from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()


def main():
    s = Solution()
    print(s.isPowerOfFour(256))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 59 ms, faster than 30.11% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 54.38% of Python3 online submissions for Power of Four.

2. Runtime: 69 ms, faster than 12.23% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 54.38% of Python3 online submissions for Power of Four.

3. Runtime: 48 ms, faster than 59.25% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.
"""

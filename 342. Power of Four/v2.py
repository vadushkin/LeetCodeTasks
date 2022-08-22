class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return 0 < n == n & 1431655765 and not (n & (n - 1))


def main():
    s = Solution()
    print(s.isPowerOfFour(256))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 37.65% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.

2. Runtime: 53 ms, faster than 46.77% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 54.38% of Python3 online submissions for Power of Four.

3. Runtime: 45 ms, faster than 66.45% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 95.34% of Python3 online submissions for Power of Four.
"""

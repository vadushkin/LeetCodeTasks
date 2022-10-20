class Solution:
    def isPowerOfTwo(self, n):
        return (n > 0) and (n & (n - 1)) == 0


def main():
    s = Solution()
    print(s.isPowerOfTwo(1024))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 57 ms, faster than 35.94% of Python3 online submissions for Power of Two.
Memory Usage: 13.9 MB, less than 53.53% of Python3 online submissions for Power of Two.

2. Runtime: 38 ms, faster than 84.76% of Python3 online submissions for Power of Two.
Memory Usage: 13.9 MB, less than 9.69% of Python3 online submissions for Power of Two.

3. Runtime: 62 ms, faster than 24.12% of Python3 online submissions for Power of Two.
Memory Usage: 13.8 MB, less than 53.53% of Python3 online submissions for Power of Two.
"""

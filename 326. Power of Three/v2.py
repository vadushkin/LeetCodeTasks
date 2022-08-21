class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0


def main():
    s = Solution()
    print(s.isPowerOfThree(27))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 133 ms, faster than 51.85% of Python3 online submissions for Power of Three.
Memory Usage: 14 MB, less than 16.98% of Python3 online submissions for Power of Three.

2. Runtime: 134 ms, faster than 50.88% of Python3 online submissions for Power of Three.
Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions for Power of Three.

3. Runtime: 72 ms, faster than 98.16% of Python3 online submissions for Power of Three.
Memory Usage: 13.9 MB, less than 57.97% of Python3 online submissions for Power of Three.
"""

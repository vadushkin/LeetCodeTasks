class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 1073741824 == 4 ** 15
        return n > 0 and 1073741824 % n == 0 and str(n ** 0.5)[-2:] == '.0'


def main():
    s = Solution()
    print(s.isPowerOfFour(4))


print(4 ** 15)
if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 37 ms, faster than 86.41% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 10.18% of Python3 online submissions for Power of Four.

2. Runtime: 53 ms, faster than 46.77% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.

3. Runtime: 57 ms, faster than 35.23% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four."""

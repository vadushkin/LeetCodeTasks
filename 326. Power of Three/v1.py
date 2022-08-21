class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        for i in range(31):
            if 3 ** i == n:
                return True
        return False


def main():
    s = Solution()
    print(s.isPowerOfThree(27))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 245 ms, faster than 9.24% of Python3 online submissions for Power of Three.
Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions for Power of Three.

2. Runtime: 471 ms, faster than 5.01% of Python3 online submissions for Power of Three.
Memory Usage: 13.8 MB, less than 57.97% of Python3 online submissions for Power of Three.
"""

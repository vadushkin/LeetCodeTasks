class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in (6, 28, 496, 8128, 33550336)


def main():
    s = Solution()
    print(s.checkPerfectNumber(28))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 44 ms, faster than 86.20% of Python3 online submissions for Perfect Number.
Memory Usage: 13.9 MB, less than 57.38% of Python3 online submissions for Perfect Number.

2. Runtime: 32 ms, faster than 97.99% of Python3 online submissions for Perfect Number.
Memory Usage: 13.8 MB, less than 96.59% of Python3 online submissions for Perfect Number.
"""

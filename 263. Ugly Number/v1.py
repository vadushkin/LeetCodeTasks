class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n /= p
        return n == 1


def main():
    s = Solution()
    print(s.isUgly(125))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 28 ms, faster than 98.34% of Python3 online submissions for Ugly Number.
Memory Usage: 13.8 MB, less than 57.84% of Python3 online submissions for Ugly Number.

2. Runtime: 65 ms, faster than 18.00% of Python3 online submissions for Ugly Number.
Memory Usage: 13.9 MB, less than 12.13% of Python3 online submissions for Ugly Number.
"""

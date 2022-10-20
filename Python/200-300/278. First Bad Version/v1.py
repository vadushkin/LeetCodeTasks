def isBadVersion(mid):
    return mid


class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


def main():
    s = Solution()
    print(s.firstBadVersion(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 29.58% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 62.31% of Python3 online submissions for First Bad Version.

2. Runtime: 38 ms, faster than 79.84% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 96.96% of Python3 online submissions for First Bad Version.
"""

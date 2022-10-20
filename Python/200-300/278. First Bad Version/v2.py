import bisect


def isBadVersion(key):
    return key


class Solution(dict):
    def firstBadVersion(self, n):
        return bisect.bisect_left(self, True, 1, n)

    def __getitem__(self, key):
        return isBadVersion(key)


def main():
    s = Solution()
    print(s.firstBadVersion(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 30 ms, faster than 94.49% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 62.31% of Python3 online submissions for First Bad Version.    

2. Runtime: 51 ms, faster than 52.11% of Python3 online submissions for First Bad Version.
Memory Usage: 13.9 MB, less than 62.31% of Python3 online submissions for First Bad Version.
"""

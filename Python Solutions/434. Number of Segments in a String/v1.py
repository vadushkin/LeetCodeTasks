class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


def main():
    s = Solution()
    print(s.countSegments("Hello, my name is Gustavo"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 62 ms, faster than 14.50% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.9 MB, less than 49.05% of Python3 online submissions for Number of Segments in a String.

2. Runtime: 60 ms, faster than 21.16% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.7 MB, less than 99.63% of Python3 online submissions for Number of Segments in a String.
"""

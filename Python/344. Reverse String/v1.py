class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


def main():
    s = Solution()
    print(s.reverseString(["h", "e", "l", "l", "o"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 203 ms, faster than 95.62% of Python3 online submissions for Reverse String.
Memory Usage: 18.6 MB, less than 14.60% of Python3 online submissions for Reverse String.

2. Runtime: 456 ms, faster than 22.82% of Python3 online submissions for Reverse String.
Memory Usage: 18.7 MB, less than 14.60% of Python3 online submissions for Reverse String.
"""

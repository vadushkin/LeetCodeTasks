class Solution:
    def reverseString(self, s: list[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


def main():
    s = Solution()
    print(s.reverseString(['1', '2', '3']))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 449 ms, faster than 24.47% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 20.90% of Python3 online submissions for Reverse String.

2. Runtime: 203 ms, faster than 95.62% of Python3 online submissions for Reverse String.
Memory Usage: 18.3 MB, less than 82.82% of Python3 online submissions for Reverse String.
"""

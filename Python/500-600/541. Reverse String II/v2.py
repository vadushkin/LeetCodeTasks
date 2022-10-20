class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k) if s else ""


def main():
    s = Solution()
    print(s.reverseStr("abcdefg", 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 50 ms, faster than 68.79% of Python3 online submissions for Reverse String II.
Memory Usage: 14.2 MB, less than 5.96% of Python3 online submissions for Reverse String II.

2. Runtime: 63 ms, faster than 39.19% of Python3 online submissions for Reverse String II.
Memory Usage: 14.2 MB, less than 5.96% of Python3 online submissions for Reverse String II.
"""

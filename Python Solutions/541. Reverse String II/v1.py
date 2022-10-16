class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)


def main():
    s = Solution()
    print(s.reverseStr("abcdefg", 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 68 ms, faster than 27.65% of Python3 online submissions for Reverse String II.
Memory Usage: 14.1 MB, less than 22.57% of Python3 online submissions for Reverse String II.

2. Runtime: 39 ms, faster than 87.35% of Python3 online submissions for Reverse String II.
Memory Usage: 14.1 MB, less than 59.01% of Python3 online submissions for Reverse String II.
"""

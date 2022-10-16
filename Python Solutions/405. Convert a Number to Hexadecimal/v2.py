class Solution:
    def toHex(self, num: int) -> str:
        dt = "0123456789abcdef"
        res = []
        for i in range(8):
            res.append(dt[num & 15])
            num >>= 4
        return "".join(reversed(res)).lstrip('0') or '0'


def main():
    s = Solution()
    print(s.toHex(23))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 48 ms, faster than 53.36% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 13.9 MB, less than 61.57% of Python3 online submissions for Convert a Number to Hexadecimal.

2. Runtime: 30 ms, faster than 94.41% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 13.9 MB, less than 61.57% of Python3 online submissions for Convert a Number to Hexadecimal.
"""

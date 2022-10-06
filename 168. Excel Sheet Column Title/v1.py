class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = ''
        while int(columnNumber) > 0:
            columnNumber -= 1
            r = chr(int(columnNumber) % 26 + 65) + r
            columnNumber /= 26
        return r


def main():
    s = Solution()
    print(s.convertToTitle(701))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 69 ms, faster than 5.77% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.9 MB, less than 55.22% of Python3 online submissions for Excel Sheet Column Title.

2. Runtime: 62 ms, faster than 15.15% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.8 MB, less than 55.22% of Python3 online submissions for Excel Sheet Column Title.
"""

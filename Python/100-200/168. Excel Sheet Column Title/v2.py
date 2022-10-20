class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return "" if columnNumber == 0 else self.convertToTitle((columnNumber - 1) // 26) + chr(
            (columnNumber - 1) % 26 + ord('A'))


def main():
    s = Solution()
    print(s.convertToTitle(701))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 27.10% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.9 MB, less than 9.93% of Python3 online submissions for Excel Sheet Column Title.

2. Runtime: 46 ms, faster than 63.72% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.8 MB, less than 55.22% of Python3 online submissions for Excel Sheet Column Title.
"""

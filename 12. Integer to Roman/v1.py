class Solution:
    def intToRoman(self, num: int) -> str:
        list_roman = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                      ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        result = ""
        for sym, val in reversed(list_roman):
            if num // val:
                count = num // val
                result += (sym * count)
                num %= val

        return result


def main():
    s = Solution()
    print(s.intToRoman(43))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 81 ms, faster than 48.30% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.9 MB, less than 35.90% of Python3 online submissions for Integer to Roman.

2. Runtime: 59 ms, faster than 82.33% of Python3 online submissions for Integer to Roman.
Memory Usage: 14 MB, less than 6.82% of Python3 online submissions for Integer to Roman.
"""

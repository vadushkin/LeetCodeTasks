class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


def main():
    s = Solution()
    print(s.intToRoman(14))


if __name__ == "__main__":
    main()

"""Test:
1. Runtime: 68 ms, faster than 69.06% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.9 MB, less than 80.47% of Python3 online submissions for Integer to Roman.

2. Runtime: 58 ms, faster than 84.02% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.9 MB, less than 35.90% of Python3 online submissions for Integer to Roman.
"""

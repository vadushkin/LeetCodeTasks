class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return "0"

        ans = ""
        sign = 1 if num > 0 else -1
        num = abs(num)

        while num > 0:
            num, mod = divmod(num, 7)
            ans += f"{mod}"

        if num % 7 == 0:
            return str(int(ans[::-1]) * sign)
        return str(int(ans) * sign)


def main():
    s = Solution()
    print(s.convertToBase7(0))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 70 ms, faster than 7.82% of Python3 online submissions for Base 7.
Memory Usage: 14 MB, less than 12.79% of Python3 online submissions for Base 7.

2. Runtime: 56 ms, faster than 45.54% of Python3 online submissions for Base 7.
Memory Usage: 13.8 MB, less than 59.61% of Python3 online submissions for Base 7.
"""

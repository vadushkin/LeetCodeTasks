class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 2:
            return 0

        expression = 1

        for number in range(2, n + 1):
            expression *= number

        counter = 0
        expression = str(expression)
        i = len(expression) - 1

        while expression[i] == '0':
            counter += 1
            i -= 1

        return counter


def main():
    s = Solution()
    print(s.trailingZeroes(7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 4324 ms Beats 14.83%
   Memory 13.9 MB Beats 22.9%

2. Runtime 5295 ms Beats 11.86%
   Memory 14 MB Beats 22.9%
"""

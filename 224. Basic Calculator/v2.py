class Solution:
    def calculate(self, s: str) -> int:
        def calc(i):
            p, n, op = 0, 0, 1
            while i < len(s) and s[i] != ')':
                if s[i] == '(':
                    i, n = calc(i + 1)
                elif s[i] in '+-':
                    p, n, op = p + op * n, 0, [-1, 1][s[i] == '+']
                elif s[i] != ' ':
                    n = 10 * n + int(s[i])
                i += 1
            return i, p + op * n

        return calc(0)[1]


def main():
    s = Solution()
    print(s.calculate("(1 + 10) - 5"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 223 ms, faster than 30.36% of Python3 online submissions for Basic Calculator.
Memory Usage: 15.8 MB, less than 26.22% of Python3 online submissions for Basic Calculator.

2. Runtime: 368 ms, faster than 8.81% of Python3 online submissions for Basic Calculator.
Memory Usage: 15.8 MB, less than 29.74% of Python3 online submissions for Basic Calculator.
"""

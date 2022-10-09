class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, [1]
        for i in s + "+":
            if i.isdigit():
                num = 10 * num + int(i)
            elif i in "+-":
                res += num * sign * stack[-1]
                sign = 1 if i == "+" else -1
                num = 0
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ")":
                res += num * sign * stack[-1]
                num = 0
                stack.pop()
        return res


def main():
    s = Solution()
    print(s.calculate("1 + 10 - 3"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 176 ms, faster than 46.32% of Python3 online submissions for Basic Calculator.
Memory Usage: 15.4 MB, less than 76.49% of Python3 online submissions for Basic Calculator.

2. Runtime: 72 ms, faster than 97.49% of Python3 online submissions for Basic Calculator.
Memory Usage: 15.2 MB, less than 98.34% of Python3 online submissions for Basic Calculator.
"""

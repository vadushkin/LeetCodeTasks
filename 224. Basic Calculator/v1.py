class Solution:
    def calculate(self, s: str) -> int:
        return eval(s)


def main():
    s = Solution()
    print(s.calculate("1 + 1"))


if __name__ == "__main__":
    main()

"""Tests:
1. SyntaxError

2. SyntaxError
"""

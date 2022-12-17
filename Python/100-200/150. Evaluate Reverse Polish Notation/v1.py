class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-*/':

                second = stack.pop()
                first = stack.pop()

                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(token))

        return stack.pop()


def main():
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 70 ms Beats 91.90%
   Memory 14.3 MB Beats 60.84%

2. Runtime 97 ms Beats 74.17% 
   Memory 14.4 MB Beats 60.84%
"""

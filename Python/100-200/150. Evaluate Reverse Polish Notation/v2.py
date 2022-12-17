class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                var, second, first_stack = 0, stack.pop(), stack.pop()

                match token:
                    case "+":
                        var = first_stack + second
                    case "-":
                        var = first_stack - second
                    case "*":
                        var = first_stack * second
                    case "/":
                        var = int(first_stack / second)

                stack.append(var)

        return stack[-1]


def main():
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 80 ms Beats 80.39%
   Memory 14.5 MB Beats 8.52% 

2. Runtime 77 ms Beats 82.50%
   Memory 14.4 MB Beats 60.84%
"""

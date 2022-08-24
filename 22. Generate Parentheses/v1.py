class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return ['']
        res = []
        for num in range(n):
            for left in self.generateParenthesis(num):
                for right in self.generateParenthesis(n - 1 - num):
                    res.append(f'({left}){right}')
        return res


def main():
    s = Solution()
    print(s.generateParenthesis(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 88 ms, faster than 8.06% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.1 MB, less than 77.53% of Python3 online submissions for Generate Parentheses.

2. Runtime: 40 ms, faster than 86.32% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.2 MB, less than 77.53% of Python3 online submissions for Generate Parentheses.
"""

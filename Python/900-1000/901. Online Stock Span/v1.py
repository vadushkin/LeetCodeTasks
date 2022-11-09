class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]

        self.stack.append([price, ans])
        return ans


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1115 ms Beats 23.8%
   Memory 19.5 MB Beats 39.40%

2. Runtime 400 ms Beats 99.57%
   Memory 19.6 MB Beats 39.40%
"""

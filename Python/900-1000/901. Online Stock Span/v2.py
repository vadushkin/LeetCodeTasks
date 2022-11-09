class StockSpanner:
    def __init__(self):
        self.stack = [[float("inf"), 0]]

    def next(self, price: int) -> int:
        curDay = self.stack[-1][1] + 1

        while price >= self.stack[-1][0]:
            self.stack.pop(-1)

        res = curDay - self.stack[-1][1]
        self.stack.append([price, curDay])

        return res


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1233 ms Beats 8.25%
   Memory 19.5 MB Beats 39.40%

2. Runtime 1233 ms Beats 8.25%
   Memory 19.5 MB Beats 39.40%
"""

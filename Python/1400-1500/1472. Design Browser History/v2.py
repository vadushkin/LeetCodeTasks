class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


def main():
    bh = BrowserHistory("leetcode.com")

    bh.visit("google.com")
    bh.visit("facebook.com")
    bh.visit("youtube.com")

    bh.back(1)
    bh.back(1)

    bh.forward(1)
    bh.visit("linkedin.com")
    bh.forward(2)

    bh.back(2)
    bh.back(7)


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 226 ms Beats 74.42% 
   Memory 16.6 MB Beats 70.44%

2. Runtime 216 ms Beats 88.31% 
   Memory 16.6 MB Beats 70.44%
"""

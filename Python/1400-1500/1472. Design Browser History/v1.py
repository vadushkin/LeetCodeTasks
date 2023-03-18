class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack = [""] * 5005
        self.stack[0] = homepage

        self.current_page = 0
        self.last_page = 0

    def visit(self, url: str) -> None:
        self.current_page += 1
        self.last_page = self.current_page

        self.stack[self.current_page] = url

    def back(self, steps: int) -> str:
        self.current_page = max(0, self.current_page - steps)
        return self.stack[self.current_page]

    def forward(self, steps: int) -> str:
        self.current_page = min(self.last_page, self.current_page + steps)
        return self.stack[self.current_page]


def main():
    bh = BrowserHistory("leetcode.com")

    print(bh.visit("google.com"))
    print(bh.visit("facebook.com"))
    print(bh.visit("youtube.com"))

    print(bh.back(1))
    print(bh.back(1))

    print(bh.forward(1))
    print(bh.visit("linkedin.com"))
    print(bh.forward(2))

    print(bh.back(2))
    print(bh.back(7))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 213 ms Beats 92.45% 
   Memory 16.7 MB Beats 70.44%

2. Runtime 220 ms Beats 82.13% 
   Memory 16.6 MB Beats 70.44%
"""

class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 34 ms Beats 87.2%
   Memory 13.9 MB Beats 76.9%

2. Runtime 29 ms Beats 95.15% 
   Memory 14 MB Beats 76.9%
"""

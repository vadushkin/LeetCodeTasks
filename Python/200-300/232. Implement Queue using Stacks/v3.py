class MyQueue:
    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        self.frontToBack()
        return self.front.pop()

    def peek(self) -> int:
        self.frontToBack()
        return self.front[-1]

    def empty(self) -> bool:
        return len(self.front) + len(self.back) == 0

    def frontToBack(self) -> None:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 42 ms Beats 12.9% 
   Memory 13.9 MB Beats 64.72%

2. Runtime 35 ms Beats 42.86% 
   Memory 14 MB Beat 64.72%
"""

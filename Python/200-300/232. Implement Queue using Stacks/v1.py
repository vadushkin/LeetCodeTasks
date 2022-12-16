from collections import deque


class MyQueue:
    def __init__(self):
        self._list = deque([])

    def push(self, x: int) -> None:
        self._list.append(x)

    def pop(self) -> int:
        return self._list.popleft()

    def peek(self) -> int:
        return self._list[0]

    def empty(self) -> bool:
        return len(self._list) > 0


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 27 ms Beats 97.36%
   Memory 13.9 MB Beats 98.86%

2. Runtime 33 ms Beats 89.28%
   Memory 14.1 MB Beats 24.53%
"""

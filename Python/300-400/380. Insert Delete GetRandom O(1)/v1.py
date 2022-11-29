import random


class RandomizedSet:
    def __init__(self):
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return True

        self.lst.append(val)
        return False

    def remove(self, val: int) -> bool:
        if val not in self.lst:
            return False

        self.lst.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst) if self.lst else None


def main():
    ...


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2203 ms Beats 5.2%
   Memory 61.4 MB Beats 57.51%

2. Runtime 1720 ms Beats 8.19%
   Memory 61.3 MB Beats 57.51%
"""

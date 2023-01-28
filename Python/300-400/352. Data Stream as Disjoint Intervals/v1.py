from collections import defaultdict


class SummaryRanges:
    def __init__(self):
        def cmp():
            return -1

        self.mp = defaultdict(cmp)
        self.a = []

    def addNum(self, value: int) -> None:
        if self.mp[value] != -1:
            return

        if self.mp[value - 1] != -1:
            self.a.remove([self.mp[value - 1], value - 1])
            self.mp[value] = self.mp[value - 1]
            self.mp[self.mp[value - 1]] = value
            self.a.append([self.mp[value], value])

            if self.mp[value + 1] != -1:
                self.a.remove([self.mp[value], value])
                self.a.remove([value + 1, self.mp[value + 1]])
                self.a.append([self.mp[value], self.mp[value + 1]])
                self.mp[self.mp[value]] = self.mp[value + 1]
                self.mp[self.mp[value + 1]] = self.mp[value]

        elif self.mp[value + 1] != -1:
            self.a.remove([value + 1, self.mp[value + 1]])
            self.mp[value] = self.mp[value + 1]
            self.mp[self.mp[value + 1]] = value
            self.a.append([value, self.mp[value]])

        if self.mp[value] == -1:
            self.mp[value] = value
            self.a.append([value, value])

    def getIntervals(self) -> list[list[int]]:
        return sorted(self.a)


def main():
    pass


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 233 ms Beats 49.83% 
   Memory 19.1 MB Beats 43.48%

2. Runtime 155 ms Beats 94.31%
   Memory 19.1 MB Beats 43.48%
"""

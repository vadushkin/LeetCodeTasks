class DSU:
    def __init__(self):
        self.p = {}
        self.intervals = {}

    def exists(self, x):
        return x in self.p

    def make_set(self, x):
        self.p[x] = x
        self.intervals[x] = [x, x]

    def find(self, x):
        if not self.exists(x):
            return None

        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)

        if xr is None or yr is None:
            return

        self.p[xr] = yr
        x_interval = self.intervals[xr]

        del self.intervals[xr]

        self.intervals[yr] = [min(self.intervals[yr][0], x_interval[0]), max(self.intervals[yr][1], x_interval[1])]


class SummaryRanges:
    def __init__(self):
        self.dsu = DSU()

    def addNum(self, val: int) -> None:
        if self.dsu.exists(val):
            return

        self.dsu.make_set(val)

        self.dsu.union(val, val - 1)
        self.dsu.union(val, val + 1)

    def getIntervals(self) -> list[list[int]]:
        return sorted(self.dsu.intervals.values())


def main():
    pass


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 171 ms Beats 73.58%
   Memory 19 MB Beats 43.48%

2. Runtime 167 ms Beats 80.27%
   Memory 19 MB Beats 43.48%
"""

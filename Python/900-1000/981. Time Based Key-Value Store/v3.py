import bisect
import collections


class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]


def main():
    s = TimeMap()
    # print(s.get())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1524 ms, faster than 39.75% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 68.2 MB, less than 97.70% of Python3 online submissions for Time Based Key-Value Store.

2. Runtime: 950 ms, faster than 76.50% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 68.2 MB, less than 97.06% of Python3 online submissions for Time Based Key-Value Store.
"""

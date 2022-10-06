class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_time_map:
            self.key_time_map[key] = []
        self.key_time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map:
            return ""
        if timestamp < self.key_time_map[key][0][0]:
            return ""
        left = 0
        right = len(self.key_time_map[key])
        while left < right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.key_time_map[key][right - 1][1]


def main():
    s = TimeMap()
    # print(s.get())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1006 ms, faster than 72.51% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 72.2 MB, less than 38.03% of Python3 online submissions for Time Based Key-Value Store.

2. Runtime: 1524 ms, faster than 39.75% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 72.3 MB, less than 34.33% of Python3 online submissions for Time Based Key-Value Store.
"""

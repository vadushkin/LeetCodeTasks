class MedianFinder:
    def __init__(self):
        self._arr = []

    def addNum(self, num: int) -> None:
        self._arr.append(num)

    def findMedian(self) -> float:
        self._arr.sort()
        len_arr = len(self._arr)

        if len_arr % 2 == 1:
            return self._arr[len_arr // 2]
        return (self._arr[(len_arr // 2) - 1] + self._arr[len_arr // 2]) / 2


"""Tests:
1. Runtime 7420 ms Beats 5%
   Memory 36 MB Beats 66.11%

2. Runtime 7500 ms Beats 5%
   Memory 35.7 MB Beats 80.22%
"""

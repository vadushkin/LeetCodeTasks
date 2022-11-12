from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

        return -self.maxHeap[0]


"""Tests:
1. Runtime 1215 ms Beats 63.6%
   Memory 36.2 MB Beats 32.61%

2. Runtime 509 ms Beats 98.87%
   Memory 36.2 MB Beats 32.61% 
"""

import heapq

class KthLargest:
    def init(self, k: int, nums: List[int]):

        self.heap = []

        self.k = k

        for num in nums:

            self.add(num)


    def add(self, val: int) -> int:
       
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

import collections
import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = collections.Counter(words)
        heap = [(-count, word) for word, count in counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


def main():
    s = Solution()
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 122 ms, faster than 37.74% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 14 MB, less than 27.71% of Python3 online submissions for Top K Frequent Words.

2. Runtime: 109 ms, faster than 55.92% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 14.1 MB, less than 27.71% of Python3 online submissions for Top K Frequent Words.
"""

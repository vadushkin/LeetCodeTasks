from heapq import heapify, heappop, heappush


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        heap = list(set(-(num * 2 if num & 1 else num) for num in nums))
        heapify(heap)
        ma, mi = -heap[0], -max(heap)
        ans = ma - mi

        while heap[0] % 2 == 0:
            x = heappop(heap) // 2
            heappush(heap, x)
            ma, mi = -heap[0], min(mi, -x)
            ans = min(ans, ma - mi)

        return ans


def main():
    s = Solution()
    print(s.minimumDeviation([1, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 675 ms Beats 97.1% 
   Memory 22.8 MB Beats 38.81%

2. Runtime 715 ms Beats 94.3% 
   Memory 23 MB Beats 34.33%
"""

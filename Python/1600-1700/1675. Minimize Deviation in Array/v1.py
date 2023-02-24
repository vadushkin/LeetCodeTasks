import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        pq = []

        for num in nums:
            heapq.heappush(pq, [num // (num & -num), num])

        res = float('inf')
        pq_max = max(num for num, num0 in pq)

        while len(pq) == len(nums):
            num, num0 = heapq.heappop(pq)
            res = min(res, pq_max - num)

            if num % 2 == 1 or num < num0:
                pq_max = max(pq_max, num * 2)
                heapq.heappush(pq, [num * 2, num0])

        return res


def main():
    s = Solution()
    print(s.minimumDeviation([1, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 3235 ms Beats 28.36% 
   Memory 23.7 MB Beats 23.88%

2. Runtime 3235 ms Beats 28.36% 
   Memory 23.6 MB Beats 23.88%
"""

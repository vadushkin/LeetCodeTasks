from heapq import heappop, heappush


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n = len(nums)
        min_heap = [(0, -1)]
        pre_sum_so_far = 0
        ans = nums[0]

        for i in range(2 * n):
            pre_sum_so_far += nums[i % n]

            while min_heap and i - min_heap[0][1] > n:
                heappop(min_heap)

            pre_sum_previous = min_heap[0][0]
            ans = max(ans, pre_sum_so_far - pre_sum_previous)
            heappush(min_heap, (pre_sum_so_far, i))

        return ans


def main():
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 854 ms Beats 36.10%
   Memory 25 MB Beats 5.16%

2. Runtime 801 ms Beats 38.2%
   Memory 25.1 MB Beats 5.16%
"""

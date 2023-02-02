from collections import Counter


class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        trips = pairs = 0
        count = Counter()

        for e, num in enumerate(nums):
            trips += pairs - count[num] * (e - count[num])
            pairs += e - count[num]
            count[num] += 1

        return trips


def main():
    s = Solution()
    print(s.unequalTriplets([4, 4, 2, 4, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 42 ms Beats 90.57% 
   Memory 13.9 MB Beats 59.27%

2. Runtime 42 ms Beats 90.57% 
   Memory 13.9 MB Beats 59.27%
"""

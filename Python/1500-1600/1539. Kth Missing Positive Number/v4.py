from bisect import bisect_left


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        return bisect_left([num - i - 1 for i, num in enumerate(arr)], k) + k


def main():
    s = Solution()
    print(s.findKthPositive([2, 3, 4, 7, 11], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 54 ms Beats 65.76% 
   Memory 14.1 MB Beats 13.3%

2. Runtime 50 ms Beats 83.51% 
   Memory 13.9 MB Beats 80.43%
"""

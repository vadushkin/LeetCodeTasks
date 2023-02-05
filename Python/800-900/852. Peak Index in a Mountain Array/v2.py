class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mi = (lo + hi) // 2

            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi

        return lo


def main():
    s = Solution()
    print(s.peakIndexInMountainArray([0, 1, 0]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 658 ms Beats 38.37% 
   Memory 27.8 MB Beats 57.7%

2. Runtime 591 ms Beats 95.48% 
   Memory 28 MB Beats 10.20%
"""

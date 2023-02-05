class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i + 1]:
                return i


def main():
    s = Solution()
    print(s.peakIndexInMountainArray([0, 2, 1, 0]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 678 ms Beats 31.97% 
   Memory 27.3 MB Beats 68.49%
   
2. Runtime 606 ms Beats 85.1% 
   Memory 27.2 MB Beats 80.25%
"""

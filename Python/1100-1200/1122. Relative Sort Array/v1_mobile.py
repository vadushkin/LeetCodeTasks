class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)


def main():
    s = Solution()
    print(s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 38 ms Beats 82.10% 
   Memory 14 MB Beats 32.53%

2. Runtime 50 ms Beats 31.20% 
   Memory 13.9 MB Beats 68.41%
"""

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)


def main():
    s = Solution()
    print(s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 114 ms Beats 55.87% 
   Memory 14.1 MB Beats 36.20%

2. Runtime 107 ms Beats 62.43% 
   Memory 14 MB Beats 36.20%
"""

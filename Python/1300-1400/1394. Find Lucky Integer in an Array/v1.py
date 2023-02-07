class Solution:
    def findLucky(self, arr: list[int]) -> int:
        for i in sorted(set(arr), reverse=True):
            if arr.count(i) == i:
                return i

        return -1


def main():
    s = Solution()
    print(s.findLucky([2, 2, 3, 4, 4, 4, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 55 ms Beats 89.23% 
   Memory 14.1 MB Beats 12.94%

2. Runtime 55 ms Beats 89.23% 
   Memory 13.8 MB Beats 90.71%
"""

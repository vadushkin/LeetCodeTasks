import collections


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        cnt = collections.Counter(arr)
        return max([k for k, v in cnt.items() if k == v] + [-1])


def main():
    s = Solution()
    print(s.findLucky([2, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 61 ms Beats 67.79% 
   Memory 13.9 MB Beats 90.71% 
   
2. Runtime 57 ms Beats 83.10% 
   Memory 13.9 MB Beats 53.36%
"""

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        return tuple(set(arr) ^ set(list(range(1, arr[-1] + k + 1))))[k - 1]


def main():
    s = Solution()
    print(s.findKthPositive([2, 3, 4, 7, 11], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 54 ms Beats 65.76% 
   Memory 14.1 MB Beats 13.3%

2. Runtime 51 ms Beats 78.47% 
   Memory 14.2 MB Beats 13.3%
"""

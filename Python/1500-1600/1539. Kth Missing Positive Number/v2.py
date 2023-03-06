class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        return list(set(range(1, 2001)) - set(arr))[k - 1]


def main():
    s = Solution()
    print(s.findKthPositive([2, 3, 4, 7, 11], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 56 ms Beats 56.56% 
   Memory 14.3 MB Beats 13.3%

2. Runtime 57 ms Beats 51.94% 
   Memory 14.2 MB Beats 13.3%
"""

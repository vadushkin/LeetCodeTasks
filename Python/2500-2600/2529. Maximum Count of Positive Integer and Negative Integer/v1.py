class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        return max(len(tuple(filter(lambda x: x > 0, nums))), len(tuple(filter(lambda x: x < 0, nums))))


def main():
    s = Solution()
    print(s.maximumCount([-2, -1, -1, 1, 2, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 138 ms Beats 21.50% 
   Memory 14.4 MB Beats 11.82%

2. Runtime 130 ms Beats 59.84%
   Memory 14.3 MB Beats 11.82%
"""

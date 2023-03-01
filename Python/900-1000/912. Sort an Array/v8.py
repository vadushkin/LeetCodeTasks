class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return sorted(nums)


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 679 ms Beats 93.53% 
   Memory 22 MB Beats 63.69%

2. Runtime 671 ms Beats 94.30% 
   Memory 22.1 MB Beats 63.69%
"""

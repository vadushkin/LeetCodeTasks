class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        return sum(c := 0 if num else c + 1 for num in [1] + nums)


def main():
    s = Solution()
    print(s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1123 ms Beats 44.52% 
   Memory 24.5 MB Beats 100%

2. Runtime 1068 ms Beats 85.87% 
   Memory 24.5 MB Beats 78.9%
"""

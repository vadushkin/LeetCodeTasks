class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [j for i in range(n) for j in [nums[i], nums[i + n]]]


def main():
    s = Solution()
    print(s.shuffle([2, 5, 1, 3, 4, 7], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 64 ms Beats 66.70% 
   Memory 14.2 MB Beats 33.52%

2. Runtime 68 ms Beats 47.71% 
   Memory 14.1 MB Beats 86.30%
"""

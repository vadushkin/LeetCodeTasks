class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nums.sort(key=bool, reverse=True)


def main():
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 0, 3, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 151 ms Beats 99.67% 
   Memory 15.5 MB Beats 56.19%

2. Runtime 151 ms Beats 99.67% 
   Memory 15.6 MB Beats 56.19%
"""

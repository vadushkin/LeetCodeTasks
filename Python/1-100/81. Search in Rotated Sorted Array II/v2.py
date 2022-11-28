class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return target in nums


def main():
    s = Solution()
    print(s.search([2, 3, 4, 5, 0, 1], 0))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 136 ms Beats 8.64%
   Memory 14.4 MB Beats 58.2%

2. Runtime 87 ms Beats 72.21%   
   Memory 14.4 MB Beats 93.63%
"""

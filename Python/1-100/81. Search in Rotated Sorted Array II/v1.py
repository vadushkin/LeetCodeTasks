class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return True if nums.count(target) > 0 else False


def main():
    s = Solution()
    print(s.search([2, 5, 6, 0, 0, 1, 2], 0))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 58 ms Beats 90.22%
   Memory 14.3 MB Beats 93.63%

2. Runtime 100 ms Beats 66.87%
   Memory 14.5 MB Beats 58.2%
"""

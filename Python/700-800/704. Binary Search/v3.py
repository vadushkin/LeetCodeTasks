class Solution:
    def search(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


def main():
    s = Solution()
    print(s.search([1, 2, 3, 3, 5], 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 244 ms Beats 81.35% 
   Memory 15.5 MB Beats 18.75%

2. Runtime 253 ms Beats 60.30% 
   Memory 15.4 MB Beats 97.31%
"""

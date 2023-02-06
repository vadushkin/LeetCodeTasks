class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [j for i in range(n) for j in nums[i::n]]


def main():
    s = Solution()
    print(s.shuffle([2, 5, 1, 3, 4, 7], 3))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 65 ms Beats 60.58% 
   Memory 14 MB Beats 86.30%
 
2. Runtime 57 ms Beats 91.91% 
   Memory 14 MB Beats 86.30%
"""

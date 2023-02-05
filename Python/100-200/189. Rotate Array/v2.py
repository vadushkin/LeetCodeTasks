class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    @staticmethod
    def reverse(nums: list[int], start: int, end: int) -> None:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1


def main():
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 230 ms Beats 68.77% 
   Memory 25.4 MB Beats 76.82%

2. Runtime 243 ms Beats 52.80% 
   Memory 25.4 MB Beats 28.80%
"""

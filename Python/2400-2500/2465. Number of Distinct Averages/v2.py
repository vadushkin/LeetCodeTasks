class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        len_of_nums, set_of_averages = len(nums), set()

        for i in range(0, len_of_nums // 2):
            set_of_averages.add((nums[i] + nums[len_of_nums - i - 1]) / 2)

        return len(set_of_averages)


def main():
    s = Solution()
    print(s.distinctAverages([4, 1, 4, 0, 3, 5]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 31 ms Beats 83.53% 
   Memory 13.9 MB Beats 9.40%

2. Runtime 31 ms Beats 83.53% 
   Memory 13.9 MB Beats 9.40%
"""

class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        sum_average = set()

        while len(nums) > 1:
            min_v = min(nums)
            max_v = max(nums)

            nums.remove(min_v)
            nums.remove(max_v)

            sum_average.add((min_v + max_v) / 2)

        return len(sum_average)


def main():
    s = Solution()
    print(s.distinctAverages([4, 1, 4, 0, 3, 5]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 46 ms Beats 27.91% 
   Memory 13.9 MB Beats 53.59%

2. Runtime 32 ms Beats 79.26% 
   Memory 13.8 MB Beats 96.41%
"""

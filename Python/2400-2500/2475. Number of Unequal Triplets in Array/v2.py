class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        triplets = 0

        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                for c in nums[j + 1:]:
                    if len(set({a, b, c})) == 3:
                        triplets += 1

        return triplets


def main():
    s = Solution()
    print(s.unequalTriplets([4, 4, 2, 4, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1108 ms Beats 28.85% 
   Memory 13.9 MB Beats 59.27%

2. Runtime 1033 ms Beats 29.96% 
   Memory 13.8 MB Beats 97.45%
"""

import random


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        while True:
            s = random.sample(nums, 2)
            if s[0] == s[1]:
                return s[0]


def main():
    s = Solution()
    print(s.repeatedNTimes([1, 2, 3, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 194 ms Beats 98.78%
   Memory 15.4 MB Beats 55.30%

2. Runtime 195 ms Beats 98.59% 
   Memory 15.4 MB Beats 55.30%
"""

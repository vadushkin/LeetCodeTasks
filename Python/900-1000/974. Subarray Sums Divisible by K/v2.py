import itertools


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        result = 0

        mod_groups = [0] * k
        mod_groups[0] = 1

        for prefixSum in itertools.accumulate(nums):
            result += mod_groups[prefixSum % k]
            mod_groups[prefixSum % k] += 1

        return result


def main():
    s = Solution()
    print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 306 ms Beats 82.45%
   Memory 18.8 MB Beats 87.93%

2. Runtime 280 ms Beats 99.35%
   Memory 18.9 MB Beats 63.55%
"""

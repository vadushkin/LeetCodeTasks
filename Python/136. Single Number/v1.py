import collections


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if not nums:
            return 0
        counter = collections.Counter(nums).most_common()
        for i in counter:
            if i[1] == 1:
                return i[0]
        return -1


def main():
    s = Solution()
    print(s.singleNumber([]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 301 ms, faster than 21.83% of Python3 online submissions for Single Number.
Memory Usage: 16.9 MB, less than 11.91% of Python3 online submissions for Single Number.

2. Runtime: 306 ms, faster than 20.91% of Python3 online submissions for Single Number.
Memory Usage: 16.9 MB, less than 11.91% of Python3 online submissions for Single Number.
"""

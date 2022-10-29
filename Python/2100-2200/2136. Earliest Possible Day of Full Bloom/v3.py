class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        ans = 0

        for g, p in sorted(zip(growTime, plantTime)):
            ans = g + p if g >= ans else ans + p

        return ans


def main():
    s = Solution()
    print(s.earliestFullBloom([1, 4, 3], [2, 3, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 5525 ms, faster than 5.16% of Python3 online submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 30.9 MB, less than 95.81% of Python3 online submissions for Earliest Possible Day of Full Bloom.

2. Runtime: 1689 ms, faster than 99.03% of Python3 online submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 30.9 MB, less than 90.65% of Python3 online submissions for Earliest Possible Day of Full Bloom.
"""

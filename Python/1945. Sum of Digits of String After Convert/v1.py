class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = [str(ord(c) - ord('a') + 1) for c in s]
        nums = ''.join(nums)
        for i in range(k):
            nums = str(sum(map(int, nums)))
        return nums


def main():
    s = Solution()
    print(s.getLucky("leetcode", 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 71 ms, faster than 33.62% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 13.9 MB, less than 74.64% of Python3 online submissions for Sum of Digits of String After Convert.

2. Runtime: 76 ms, faster than 23.30% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 13.9 MB, less than 74.64% of Python3 online submissions for Sum of Digits of String After Convert.
"""

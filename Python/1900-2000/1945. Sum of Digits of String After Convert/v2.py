class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = [str(ord(c) - ord('a') + 1) for c in s]
        for _ in range(k):
            nums = str(sum(int(digit) for num in nums for digit in num))
        return nums


def main():
    s = Solution()
    print(s.getLucky("qweasdzxc", 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 62 ms, faster than 55.34% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 13.9 MB, less than 74.64% of Python3 online submissions for Sum of Digits of String After Convert.

2. Runtime: 68 ms, faster than 42.23% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 13.8 MB, less than 98.30% of Python3 online submissions for Sum of Digits of String After Convert.
"""

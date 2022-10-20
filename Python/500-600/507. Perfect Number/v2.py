class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num == 1:
            return False

        res = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                res += i + num // i

        return res == num


def main():
    s = Solution()
    print(s.checkPerfectNumber(28))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 74 ms, faster than 46.72% of Python3 online submissions for Perfect Number.
Memory Usage: 13.9 MB, less than 11.53% of Python3 online submissions for Perfect Number.

2. Runtime: 86 ms, faster than 28.56% of Python3 online submissions for Perfect Number.
Memory Usage: 13.8 MB, less than 57.38% of Python3 online submissions for Perfect Number.
"""

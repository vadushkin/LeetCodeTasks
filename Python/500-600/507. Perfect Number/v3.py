class Solution:
    def checkPerfectNumber(self, num):

        primes = {2, 3, 5, 7, 13, 17, 19, 31}

        for item in primes:
            if (2 ** (item - 1)) * ((2 ** item) - 1) == num:
                return True

        return False


def main():
    s = Solution()
    print(s.checkPerfectNumber(28))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 27 ms, faster than 99.48% of Python3 online submissions for Perfect Number.
Memory Usage: 13.9 MB, less than 11.53% of Python3 online submissions for Perfect Number.

2. Runtime: 67 ms, faster than 55.63% of Python3 online submissions for Perfect Number.
Memory Usage: 14 MB, less than 11.53% of Python3 online submissions for Perfect Number.
"""

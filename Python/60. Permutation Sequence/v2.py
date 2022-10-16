import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])

        return permutation


def main():
    s = Solution()
    print(s.getPermutation(3, 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 34 ms, faster than 92.04% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.8 MB, less than 77.91% of Python3 online submissions for Permutation Sequence.

2. Runtime: 56 ms, faster than 48.21% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.9 MB, less than 33.63% of Python3 online submissions for Permutation Sequence.
"""

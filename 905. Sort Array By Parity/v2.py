class Solution:
    def sortArrayByParity(self, a: list[int]) -> list[int]:
        return [i for i in a if not i % 2] + [i for i in a if i % 2]


def main():
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 142 ms, faster than 33.54% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.8 MB, less than 17.33% of Python3 online submissions for Sort Array By Parity.

2. Runtime: 156 ms, faster than 20.43% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 96.46% of Python3 online submissions for Sort Array By Parity.
"""

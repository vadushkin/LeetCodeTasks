class Solution:
    def concatenatedBinary(self, n: int) -> int:
        string = ""
        for i in range(1, n + 1):
            print(bin(i))
            string += bin(i)[2:]
        return divmod(int(string, 2), 10 ** 9 + 7)[1]


def main():
    s = Solution()
    print(s.concatenatedBinary(10))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2168 ms, faster than 62.99% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 15.6 MB, less than 55.91% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.

2. Runtime: 2953 ms, faster than 42.52% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 15.7 MB, less than 45.67% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
"""

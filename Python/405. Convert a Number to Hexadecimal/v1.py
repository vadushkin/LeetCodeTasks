# class Solution:
#     def toHex(self, num: int) -> str:
#         return hex(num)[2:]

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        numbers = '0123456789abcdef'
        result = ''
        if num < 0:
            num += 2 ** 32
        while num > 0:
            digit = num % 16
            num = (num - digit) // 16
            result += str(numbers[digit])
        return result[::-1]


def main():
    s = Solution()
    print(s.toHex(-1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 39 ms, faster than 77.03% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 13.9 MB, less than 61.57% of Python3 online submissions for Convert a Number to Hexadecimal.

2. Runtime: 47 ms, faster than 56.07% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 13.8 MB, less than 97.03% of Python3 online submissions for Convert a Number to Hexadecimal.
"""

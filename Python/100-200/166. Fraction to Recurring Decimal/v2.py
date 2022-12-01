class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        negative = numerator * denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)

        quotient, remainder = divmod(numerator, denominator)
        remainders = {}
        res = [str(quotient)]

        i = 0

        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = i
            quotient, remainder = divmod(remainder * 10, denominator)
            res.append(str(quotient))
            i += 1

        if negative:
            res[0] = '-' + res[0]

        if remainder == 0:
            if len(res) == 1:
                return res[0]
            else:
                return res[0] + '.' + ''.join(res[1:])

        return res[0] + '.' + ''.join(res[1:remainders[remainder] + 1]) + '(' + ''.join(
            res[remainders[remainder] + 1:]) + ')'


def main():
    s = Solution()
    print(s.fractionToDecimal(5, 214))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 38 ms Beats 82.82%
   Memory 14 MB Beats 70.36%

2. Runtime 51 ms Beats 65.65%
   Memory 13.9 MB Beats 96.86%
"""

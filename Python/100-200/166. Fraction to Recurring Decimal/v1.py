class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        result = "" if numerator * denominator >= 0 else "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        number, numerator = divmod(numerator, denominator)
        result += str(number)

        if not numerator:
            return result

        result += "."
        result = [result]

        found = {}
        position = len(result)

        while numerator and numerator not in found:
            found[numerator] = position

            number, numerator = divmod(numerator * 10, denominator)

            result.append(str(number))

            position += 1

        if numerator in found:
            result.insert(found[numerator], '(')
            result.append(')')

        return "".join(result)


def main():
    s = Solution()
    print(s.fractionToDecimal(4, 333))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 57 ms Beats 51.36%
   Memory 14.1 MB Beats 8.9%

2. Runtime 48 ms Beats 70.27%
   Memory 14.1 MB Beats 8.9% 
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except ValueError:
            return False
        else:
            # last 9 tests ||
            # or s.lower() \/
            if s == "inf" or s == "-inf" or s == "+inf" or s == "infinity" or s == "-infinity" or s == "+infinity" or \
                    s == "Infinity" or s == "+Infinity" or s == "-Infinity":
                return False
            return True


def main():
    s = Solution()
    print(s.isNumber("-inf"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 49.21% of Python3 online submissions for Valid Number.
Memory Usage: 13.8 MB, less than 97.87% of Python3 online submissions for Valid Number.

2. Runtime: 60 ms, faster than 44.56% of Python3 online submissions for Valid Number.
Memory Usage: 13.8 MB, less than 76.21% of Python3 online submissions for Valid Number.
"""

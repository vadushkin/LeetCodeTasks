from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not (0 <= len(digits) <= 4):
            return []

        numbers_dict = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                        '8': 'tuv', '9': 'wxyz'}
        string = []
        result = []

        for digit in digits:
            if numbers_dict[digit] != '':
                string.append(numbers_dict[digit])

        if len(string):
            for i in string[0]:
                if len(string) == 1:
                    result.append(f"{i}")
                if len(string) == 2:
                    for j in string[1]:
                        result.append(f"{i}{j}")
                if len(string) == 3:
                    for j in string[1]:
                        for d in string[2]:
                            result.append(f"{i}{j}{d}")
                if len(string) == 4:
                    for j in string[1]:
                        for f in string[2]:
                            for q in string[3]:
                                result.append(f"{i}{j}{f}{q}")
        return result


def main():
    s = Solution()
    print(s.letterCombinations("2"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 38 ms, faster than 79.06% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14 MB, less than 32.00% of Python3 online submissions for Letter Combinations of a Phone Number.

2. Runtime: 37 ms, faster than 82.22% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 79.63% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

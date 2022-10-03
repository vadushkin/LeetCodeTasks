class Solution:
    def repeatedCharacter(self, string: str) -> str:
        strAlphaFreq = [0] * 26

        for char in string:
            index = ord(char) - ord('a')

            strAlphaFreq[index] += 1

            if strAlphaFreq[index] > 1:
                return char


def main():
    s = Solution()
    print(s.repeatedCharacter("asdasdasdasd"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 54 ms, faster than 36.43% of Python3 online submissions for First Letter to Appear Twice.
Memory Usage: 13.9 MB, less than 7.43% of Python3 online submissions for First Letter to Appear Twice.

2. Runtime: 45 ms, faster than 62.26% of Python3 online submissions for First Letter to Appear Twice.
Memory Usage: 13.8 MB, less than 51.40% of Python3 online submissions for First Letter to Appear Twice.
"""

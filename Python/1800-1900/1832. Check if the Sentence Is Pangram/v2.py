class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        for i in range(26):
            curr_char = chr(ord('a') + i)

            if sentence.lower().find(curr_char) == -1:
                return False

        return True


def main():
    s = Solution()
    print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 46 ms, faster than 75.12% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 14 MB, less than 11.66% of Python3 online submissions for Check if the Sentence Is Pangram.

2. Runtime: 57 ms, faster than 49.00% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 13.9 MB, less than 54.73% of Python3 online submissions for Check if the Sentence Is Pangram.
"""

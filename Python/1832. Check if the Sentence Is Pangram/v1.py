import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence.lower())) == len(string.ascii_lowercase)


def main():
    s = Solution()
    print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 68 ms, faster than 15.99% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 13.8 MB, less than 54.73% of Python3 online submissions for Check if the Sentence Is Pangram.

2. Runtime: 28 ms, faster than 97.56% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 13.9 MB, less than 11.66% of Python3 online submissions for Check if the Sentence Is Pangram.
"""

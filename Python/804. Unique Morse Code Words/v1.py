class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                    "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                    "...-", ".--", "-..-", "-.--", "--.."]

        morse_words = []

        for word in words:

            morse_word = []

            for letter in word:
                morse_word.append(alphabet[ord(letter) - ord('a')])

            morse_words.append(''.join(morse_word))

        return len(set(morse_words))


def main():
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 69 ms, faster than 40.12% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 14 MB, less than 24.64% of Python3 online submissions for Unique Morse Code Words.

2. Runtime: 73 ms, faster than 28.89% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.9 MB, less than 73.65% of Python3 online submissions for Unique Morse Code Words.
"""

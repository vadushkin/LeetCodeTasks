class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}
        return len(seen)


def main():
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 54 ms, faster than 70.67% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.9 MB, less than 73.65% of Python3 online submissions for Unique Morse Code Words.  

2. Runtime: 69 ms, faster than 40.12% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.9 MB, less than 24.64% of Python3 online submissions for Unique Morse Code Words.
"""

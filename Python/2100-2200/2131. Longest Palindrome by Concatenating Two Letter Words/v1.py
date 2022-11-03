from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:

        count = Counter(words)
        answer = 0
        central = False

        for word, cnt_of_word in count.items():
            if word[0] == word[1]:
                if cnt_of_word % 2 == 0:
                    answer += cnt_of_word
                else:
                    answer += cnt_of_word - 1
                    central = True
            elif word[0] < word[1]:
                answer += 2 * min(cnt_of_word, count[word[1] + word[0]])

        if central:
            answer += 1
        return 2 * answer


def main():
    s = Solution()
    print(s.longestPalindrome(["ab", "ba", "wr", "wr"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1897 ms, faster than 77.29% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.
Memory Usage: 38.3 MB, less than 86.56% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.

2. Runtime: 1241 ms, faster than 97.42% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.
Memory Usage: 38.2 MB, less than 86.56% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.
"""

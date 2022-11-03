class Solution:
    def longestPalindrome(self, words: list[str]) -> int:

        alphabet_size = 26
        count = [[0 for _ in range(alphabet_size)] for _ in range(alphabet_size)]

        for word in words:
            count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1

        answer = 0
        central = False

        for i in range(alphabet_size):
            if count[i][i] % 2 == 0:
                answer += count[i][i]
            else:
                answer += count[i][i] - 1
                central = True
            for j in range(i + 1, alphabet_size):
                answer += 2 * min(count[i][j], count[j][i])

        if central:
            answer += 1
        return 2 * answer


def main():
    s = Solution()
    print(s.longestPalindrome(["lc", "cl", "gg", "gg", "gg", "lc", "cl", "er"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 3804 ms, faster than 16.24% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.
Memory Usage: 38.3 MB, less than 86.56% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.

2. Runtime: 3092 ms, faster than 49.04% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.
Memory Usage: 38.2 MB, less than 86.56% of Python3 online submissions 
for Longest Palindrome by Concatenating Two Letter Words.
"""

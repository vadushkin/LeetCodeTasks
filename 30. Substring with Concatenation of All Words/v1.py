import collections


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            remaining = word_count.copy()
            words_used = 0
            for j in range(i, i + substring_size, word_length):
                sub = s[j: j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer


def main():
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 661 ms, faster than 41.77% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.1 MB, less than 97.94% of Python3 online submissions for Substring with Concatenation of All Words.

2. Runtime: 764 ms, faster than 35.70% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.1 MB, less than 75.97% of Python3 online submissions for Substring with Concatenation of All Words.
"""

import collections


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        summary, chars_counter = 0, collections.Counter(chars)

        for word in words:
            word_counter = collections.Counter(word)

            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                summary += len(word)

        return summary


def main():
    s = Solution()
    print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 155 ms Beats 66.46% 
   Memory 14.4 MB Beats 75.13%

2. Runtime 151 ms Beats 67.52% 
   Memory 14.4 MB Beats 75.13%
"""

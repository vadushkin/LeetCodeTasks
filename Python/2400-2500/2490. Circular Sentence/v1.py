class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')

        if len(sentence) == 0:
            return False

        if len(sentence) == 1:
            return sentence[0][0] == sentence[0][-1]

        first = sentence[0]
        last = sentence[-1]

        for i in range(1, len(sentence)):
            if sentence[i - 1][-1] != sentence[i][0]:
                return False

        return first[0] == last[-1]


def main():
    s = Solution()
    print(s.isCircularSentence("leetcode exercises sound delightful"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 22 ms Beats 99.68% 
   Memory 13.9 MB Beats 11.49%

2. Runtime 28 ms Beats 94.58% 
   Memory 13.9 MB Beats 11.49%
"""

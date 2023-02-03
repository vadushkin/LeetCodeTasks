class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False

        return sentence[0] == sentence[-1]


def main():
    s = Solution()
    print(s.isCircularSentence("leetcode exercises sound delightful"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 33 ms Beats 83.38% 
   Memory 13.7 MB Beats 96.70%

2. Runtime 41 ms Beats 58.90% 
   Memory 13.9 MB Beats 11.49%
"""

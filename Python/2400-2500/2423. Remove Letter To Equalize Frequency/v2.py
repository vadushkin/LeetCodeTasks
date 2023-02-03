from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            if len(set(Counter(word[0:i] + word[i + 1:]).values())) == 1:
                return True

        return False


def main():
    s = Solution()
    print(s.equalFrequency("abcc"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 35 ms Beats 59.6% 
   Memory 13.8 MB Beats 95.76%
   
2. Runtime 35 ms Beats 59.6% 
   Memory 13.8 MB Beats 95.76%
"""

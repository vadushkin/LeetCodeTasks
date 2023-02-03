from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)

        for c in word:
            counter[c] -= 1

            if counter[c] == 0:
                counter.pop(c)

            if len(set(counter.values())) == 1:
                return True

            counter[c] += 1

        return False


def main():
    s = Solution()
    print(s.equalFrequency("abbcc"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 36 ms Beats 52.87% 
   Memory 13.9 MB Beats 61.58%     
   
2. Runtime 41 ms Beats 29.93% 
   Memory 13.8 MB Beats 61.58%   
"""

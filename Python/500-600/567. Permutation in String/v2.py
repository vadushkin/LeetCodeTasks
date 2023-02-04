from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, n, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1

                if cntr[s2[i]] == 0:
                    matched += 1

            if i >= n and s2[i - n] in cntr:
                if cntr[s2[i - n]] == 0:
                    matched -= 1

                cntr[s2[i - n]] += 1

            if matched == len(cntr):
                return True

        return False


def main():
    s = Solution()
    print(s.checkInclusion("ab", "eidboaoo"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 81 ms Beats 68.64% 
   Memory 13.9 MB Beats 94.40%
   
2. Runtime 78 ms Beats 71.47% 
   Memory 14 MB Beats 28.54%
"""

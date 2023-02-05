from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []

        p_counter = Counter(p)
        s_counter = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1

            if s_counter == p_counter:
                res.append(i - len(p) + 1)

            s_counter[s[i - len(p) + 1]] -= 1

            if s_counter[s[i - len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]]

        return res


def main():
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 420 ms Beats 25.80% 
   Memory 15.1 MB Beats 74.41%

2. Runtime 391 ms Beats 28.82% 
   Memory 15.2 MB Beats 27%
"""

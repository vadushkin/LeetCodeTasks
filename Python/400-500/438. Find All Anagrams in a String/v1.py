from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        hash_map, res, len_p, len_s = defaultdict(int), [], len(p), len(s)

        if len_p > len_s:
            return []

        for ch in p:
            hash_map[ch] += 1

        for i in range(len_p - 1):
            if s[i] in hash_map:
                hash_map[s[i]] -= 1

        for i in range(-1, len_s - len_p + 1):
            if i > -1 and s[i] in hash_map:
                hash_map[s[i]] += 1

            if i + len_p < len_s and s[i + len_p] in hash_map:
                hash_map[s[i + len_p]] -= 1

            if all(v == 0 for v in hash_map.values()):
                res.append(i + 1)

        return res


def main():
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 165 ms Beats 60.38% 
   Memory 15.2 MB Beats 74.41%

2. Runtime 174 ms Beats 57.75% 
   Memory 15.2 MB Beats 74.41%
"""

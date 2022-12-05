class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True


def main():
    s = Solution()
    print(s.isIsomorphic("bbbaaaba", "aaabbbba"))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 80 ms Beats 54.15%
   Memory 14.2 MB Beats 89.33%
   
2. Runtime 96 ms Beats 31.32%
   Memory 14.1 MB Beats 99.56%
"""

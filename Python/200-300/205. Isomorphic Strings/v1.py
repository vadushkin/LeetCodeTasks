import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cntr_s = collections.Counter(s)
        cntr_t = collections.Counter(t)

        return list(cntr_s.values()) == list(cntr_t.values())


def main():
    s = Solution()
    print(s.isIsomorphic("egg", "foo"))


if __name__ == "__main__":
    main()

"""Tests: 
1. Wrong Answer
   41 / 44 testcases passed

2. Wrong Answer
   41 / 44 testcases passed
"""

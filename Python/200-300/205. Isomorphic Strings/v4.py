class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


def main():
    s = Solution()
    print(s.isIsomorphic("egg", "all"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 65 ms Beats 72.29%
   Memory 14.2 MB Beats 46.79%

2. Runtime 61 ms Beats 75.24%
   Memory 14.3 MB Beats 46.79%
"""

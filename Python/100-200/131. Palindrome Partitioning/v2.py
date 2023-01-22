import collections


class Solution:
    def __init__(self):
        self.memory = collections.defaultdict(list)

    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[]]

        if s in self.memory:
            return self.memory[s]

        ans = []

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:

                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)

        self.memory[s] = ans

        return ans


def main():
    s = Solution()
    print(s.partition("aab"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 918 ms Beats 38.3%
   Memory 32.4 MB Beats 13.16%
   
2. Runtime 1039 ms Beats 34.85%
   Memory 32.3 MB Beats 13.16%
"""

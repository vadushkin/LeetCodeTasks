from collections import defaultdict


class Solution:
    def oddString(self, words: list[str]) -> str:
        eq = defaultdict(list)

        for w in words:
            diff = [ord(a) - ord(b) for a, b in zip(w[:-1], w[1:])]
            eq[tuple(diff)].append(w)

        for _, ws in eq.items():
            if len(ws) == 1:
                return ws[0]


def main():
    s = Solution()
    print(s.oddString(["adc", "wzy", "abc"]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 43 ms Beats 48.19% 
   Memory 13.9 MB Beats 29.46%

2. Runtime 44 ms Beats 46.38% 
   Memory 13.8 MB Beats 71.45%
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        t1, t2 = self.isSub(a, b), self.isSub(b, a)

        if t1 and t2:
            return max(len(a), len(b))

        if t1:
            return len(a)

        if t2:
            return len(b)
        return -1

    def isSub(self, x, y):
        i = j = 0
        while i < len(x) and j < len(y):
            if x[i] == y[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i != len(x)


def main():
    s = Solution()
    print(s.findLUSlength("aba", "cdc"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 62.69% of Python3 online submissions for Longest Uncommon Subsequence I.
Memory Usage: 13.9 MB, less than 58.77% of Python3 online submissions for Longest Uncommon Subsequence I.

2. Runtime: 53 ms, faster than 50.43% of Python3 online submissions for Longest Uncommon Subsequence I.
Memory Usage: 13.9 MB, less than 11.75% of Python3 online submissions for Longest Uncommon Subsequence I.
"""

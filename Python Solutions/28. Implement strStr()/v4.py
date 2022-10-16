class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        t = needle

        S = set()
        M = len(t)
        d = {}

        for i in range(M - 2, -1, -1):
            if t[i] not in S:
                d[t[i]] = M - i - 1
                S.add(t[i])

        if t[M - 1] not in S:
            d[t[M - 1]] = M

        d['*'] = M

        a = haystack
        N = len(a)

        if N >= M:
            i = M - 1

            while i < N:
                k = 0
                flBreak = False
                for j in range(M - 1, -1, -1):
                    if a[i - k] != t[j]:
                        if j == M - 1:
                            off = d[a[i]] if d.get(a[i], False) else d['*']
                        else:
                            off = d[t[j]]

                        i += off
                        flBreak = True
                        break

                    k += 1

                if not flBreak:
                    return i - k + 1
            else:
                return -1
        else:
            return -1


def main():
    s = Solution()
    print(s.strStr("beautiful data", "data"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, 
faster than 60.94% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 14 MB, 
less than 17.35% of Python3 online submissions for Find the Index of the First Occurrence in a String.

2. Runtime: 57 ms, 
faster than 38.83% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 13.8 MB, 
less than 65.44% of Python3 online submissions for Find the Index of the First Occurrence in a String.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP:
        https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
        """
        p = [0] * len(needle)
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                p[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    p[i] = 0
                    i += 1
                else:
                    j = p[j - 1]

        j = i = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - len(needle)
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    i += 1

        if i == len(haystack):
            return -1


def main():
    s = Solution()
    print(s.strStr("hello my dear friend", "friend"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 83 ms,
faster than 5.67% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 13.9 MB, 
less than 65.44% of Python3 online submissions for Find the Index of the First Occurrence in a String. 

2. Runtime: 79 ms, 
faster than 5.67% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 13.9 MB, 
less than 17.35% of Python3 online submissions for Find the Index of the First Occurrence in a String.
"""

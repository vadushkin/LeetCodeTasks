class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g, s = sorted(g), sorted(s)
        i, j = 0, 0
        while i != len(g) and j != len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i


def main():
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 2, 3, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 385 ms, faster than 24.98% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.9 MB, less than 47.08% of Python3 online submissions for Assign Cookies.

2. Runtime: 166 ms, faster than 96.85% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.9 MB, less than 16.17% of Python3 online submissions for Assign Cookies.
"""

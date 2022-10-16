class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


def main():
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 361 ms, faster than 32.27% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.9 MB, less than 47.08% of Python3 online submissions for Assign Cookies.

2. Runtime: 349 ms, faster than 36.75% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.8 MB, less than 82.57% of Python3 online submissions for Assign Cookies.
"""

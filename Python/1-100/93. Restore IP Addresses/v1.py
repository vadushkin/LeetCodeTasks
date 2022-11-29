class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        path = ["" for _ in range(4)]

        self.dfs(s, 0, path, res)

        return res

    def dfs(self, s: str, level: int, path: list[str], res: list[str]) -> None:
        if not s:
            return

        if level == 3:
            path[level] = s
            if len(path[level]) <= 3 and str(int(path[level])) == path[level] and int(path[level]) <= 255:
                res.append('.'.join(path))
            return

        for i in range(1, 4):
            path[level] = s[:i]
            if str(int(path[level])) == path[level] and int(path[level]) <= 255:
                self.dfs(s[i:], level + 1, path, res)


def main():
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 65 ms Beats 59.77%
   Memory 13.9 MB Beats 36.94%

2. Runtime 66 ms Beats 57.28%
   Memory 14 MB Beats 36.94%
"""

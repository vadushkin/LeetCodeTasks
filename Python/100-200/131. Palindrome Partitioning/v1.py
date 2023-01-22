class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]


def main():
    s = Solution()
    print(s.partition("aab"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 671 ms Beats 79.61% 
   Memory 28.8 MB Beats 96.27%
   
2. Runtime 693 ms Beats 62.63% 
   Memory 28.8 MB Beats 98.71%
"""

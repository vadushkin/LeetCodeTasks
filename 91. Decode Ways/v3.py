from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            if len(string) > 0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first + second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum


def main():
    s = Solution()
    print(s.numDecodings("17331"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 67 ms, faster than 22.46% of Python3 online submissions for Decode Ways.
Memory Usage: 14.3 MB, less than 10.63% of Python3 online submissions for Decode Ways.

2. Runtime: 40 ms, faster than 82.29% of Python3 online submissions for Decode Ways.
Memory Usage: 14.3 MB, less than 10.63% of Python3 online submissions for Decode Ways.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        window_counts = {}

        l, r = 0, 0
        formed = 0

        ans = float("inf"), None, None

        while r < len(s):

            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


def main():
    s = Solution()
    print(s.minWindow("ABCDEFABDC", "ABC"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 160 ms, faster than 75.17% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.7 MB, less than 36.77% of Python3 online submissions for Minimum Window Substring.

2. Runtime: 300 ms, faster than 34.23% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.7 MB, less than 83.90% of Python3 online submissions for Minimum Window Substring.
"""

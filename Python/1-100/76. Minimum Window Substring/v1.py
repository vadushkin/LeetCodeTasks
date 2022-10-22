class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans = []

        for i in range(len(s)):
            if s[i] in t:

                t_list = list(t)
                t_list.remove(s[i])

                if not t_list:
                    ans.append(s[i])

                for j in range(i + 1, len(s)):

                    if s[j] in t_list:
                        t_list.remove(s[j])

                    if not t_list:
                        ans.append(s[i:j + 1])

        return min(ans, key=len) if ans else ""


def main():
    s = Solution()
    print(s.minWindow("a", "aa"))


if __name__ == "__main__":
    main()

"""Tests:
1. Memory Limit Exceeded 264 / 266 test cases passed.

2. Memory Limit Exceeded 265 / 266 test cases passed.
"""

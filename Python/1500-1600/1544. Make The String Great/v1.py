class Solution:
    def makeGood(self, s: str) -> str:

        while len(s) > 1:
            find = False
            for i in range(len(s) - 1):
                curr_char, next_char = s[i], s[i + 1]

                if abs(ord(curr_char) - ord(next_char)) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break

            if not find:
                break

        return s


def main():
    s = Solution()
    print(s.makeGood("abBAcC"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 83 ms Beats 17.19%
   Memory 13.9 MB Beats 61.93%

2. Runtime N/A Beats N/A (23 ms, 99.83%)
   Memory N/A Beats N/A (13.6 mb, 99.24%)
"""

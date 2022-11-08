class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood(s[:i] + s[i + 2:])

        return s


def main():
    s = Solution()
    print(s.makeGood("aaAAaaVV"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 81 ms Beats 19.85%
   Memory 13.8 MB Beats 61.93%

2. Runtime 73 ms Beats 40.29% 
   Memory 13.9 MB Beats 61.93%
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip().split(" ")
        b = []

        for i in a:
            if i != "":
                b.insert(0, i)

        return ' '.join(b)


def main():
    s = Solution()
    print(s.reverseWords(" SO GOOD EXAMPLE "))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 56 ms Beats 65.80%
   Memory 14.1 MB Beats 16.15%

2. Runtime 27 ms Beats 98.98%
   Memory 13.9 MB Beats 78.97%
"""

class Solution:
    def sumGame(self, num: str) -> bool:
        return sum([1, -1][i < len(num) / 2] * (4.5 if c == '?' else int(c)) for i, c in enumerate(num)) != 0


def main():
    s = Solution()
    print(s.sumGame("5023"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 919 ms Beats 5.68%
   Memory 14.7 MB Beats 80.68%

2. Runtime 740 ms Beats 6.82%
   Memory 15.2 MB Beats 23.86%
"""

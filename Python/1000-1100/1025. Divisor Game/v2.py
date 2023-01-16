class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0  # not n % 2


def main():
    s = Solution()
    print(s.divisorGame(2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 25 ms Beats 96.67%
   Memory 13.8 MB Beats 94.67%

2. Runtime 38 ms Beats 66.64% 
   Memory 13.8 MB Beats 49.93% 
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in self.combine(i - 1, k - 1)]


def main():
    s = Solution()
    print(s.combine(4, 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 198 ms Beats 86.11%
   Memory 16.2 MB Beats 7.2%

2. Runtime 222 ms Beats 83.32%
   Memory 16.2 MB Beats 7.2%
"""

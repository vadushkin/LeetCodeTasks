class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        Sa, Sb = sum(aliceSizes), sum(bobSizes)
        set_bob_sizes = set(bobSizes)
        for x in aliceSizes:
            if x + (Sb - Sa) // 2 in set_bob_sizes:
                return [x, int(x + (Sb - Sa) / 2)]


def main():
    s = Solution()
    print(s.fairCandySwap([1, 1], [2, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 865 ms, faster than 34.09% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.4 MB, less than 71.99% of Python3 online submissions for Fair Candy Swap.

2. Runtime: 965 ms, faster than 26.16% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.5 MB, less than 46.03% of Python3 online submissions for Fair Candy Swap.
"""

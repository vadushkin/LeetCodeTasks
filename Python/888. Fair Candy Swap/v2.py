class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        dif = (sum(aliceSizes) - sum(bobSizes)) / 2
        set_alice_s = set(aliceSizes)
        for b in set(bobSizes):
            if dif + b in set_alice_s:
                return [int(dif + b), b]


def main():
    s = Solution()
    print(s.fairCandySwap([1, 0, 2], [3, 3, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 856 ms, faster than 34.48% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.8 MB, less than 16.26% of Python3 online submissions for Fair Candy Swap.

2. Runtime: 819 ms, faster than 38.69% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 17 MB, less than 7.93% of Python3 online submissions for Fair Candy Swap.
"""

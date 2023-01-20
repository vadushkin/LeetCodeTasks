class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]] | set[tuple[int]]:
        n = len(nums)
        result = set()

        for bitmask in range(1, 1 << n):
            sequence = [nums[i] for i in range(n) if (bitmask >> i) & 1]

            if len(sequence) >= 2 and all([sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1)]):
                result.add(tuple(sequence))

        return result


def main():
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1267 ms Beats 8.29% 
   Memory 22.5 MB Beats 32.34%

2. Runtime 1260 ms Beats 8.29% 
   Memory 22.4 MB Beats 32.34%
"""

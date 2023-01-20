class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]] | set[tuple[int]]:
        result: set = set()
        sequence: list = []

        def backtrack(index: int) -> None:
            if index == len(nums):
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return

            if not sequence or sequence[-1] <= nums[index]:
                sequence.append(nums[index])
                backtrack(index + 1)
                sequence.pop()

            backtrack(index + 1)

        backtrack(0)
        return result


def main():
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 234 ms Beats 72.3%
   Memory 22.7 MB Beats 22.66%

2. Runtime 246 ms Beats 63.13% 
   Memory 22.8 MB Beats 22.66%
"""

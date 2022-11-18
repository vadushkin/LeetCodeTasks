class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        result = True

        for bit in bits[-2::-1]:
            if not bit:
                break

            result = not result

        return result


def main():
    s = Solution()
    print(s.isOneBitCharacter([1, 0, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 84 ms Beats 72.36%
   Memory 13.9 MB Beats 78.90%

2. Runtime 60 ms Beats 83.6%
   Memory 13.8 MB Beats 98.22%
"""

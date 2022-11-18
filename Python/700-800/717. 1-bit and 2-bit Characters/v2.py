class Solution:
    def isOneBitCharacter(self, b: list[int]) -> bool:
        length, index = len(b) - 1, 0
        while index < length:
            index += 1 + b[index]

        return True if index == length else False


def main():
    s = Solution()
    print(s.isOneBitCharacter([1, 0, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 111 ms Beats 41.46%
   Memory 13.8 MB Beats 78.90%

2. Runtime 102 ms Beats 57.6%
   Memory 13.8 MB Beats 78.90%
"""

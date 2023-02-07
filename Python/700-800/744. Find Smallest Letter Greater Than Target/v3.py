class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c

        return letters[0]


def main():
    s = Solution()
    print(s.nextGreatestLetter(["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "q"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 111 ms Beats 76.34% 
   Memory 14.2 MB Beats 74.68%

2. Runtime 101 ms Beats 98.35% 
   Memory 14.2 MB Beats 99.19%
"""

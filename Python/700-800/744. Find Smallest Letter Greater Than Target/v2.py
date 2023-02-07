class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        seen = set(letters)

        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))

            if cand in seen:
                return cand


def main():
    s = Solution()
    print(s.nextGreatestLetter(["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "q"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 123 ms Beats 31.35% 
   Memory 14.3 MB Beats 74.68%

2. Runtime 110 ms Beats 79.75% 
   Memory 14.3 MB Beats 74.68%
"""

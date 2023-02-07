import bisect


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


def main():
    s = Solution()
    print(s.nextGreatestLetter(["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "q"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 119 ms Beats 42.72% 
   Memory 14.3 MB Beats 74.68%

2. Runtime 115 ms Beats 58.78% 
   Memory 14.3 MB Beats 74.68%
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c * s.count(c) for c in sorted(set(s), key=s.count, reverse=True))


def main():
    s = Solution()
    print(s.frequencySort("loveleetcode"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 83 ms Beats 61.4% 
   Memory 15.2 MB Beats 81.15%

2. Runtime 88 ms Beats 54.96%
   Memory 15.2 MB Beats 98.50%
"""

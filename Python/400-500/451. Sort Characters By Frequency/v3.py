import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(item * count for item, count in sorted(collections.Counter(s).items(),
                                                              key=lambda x: x[1], reverse=True))


def main():
    s = Solution()
    print(s.frequencySort("iloveleetcode"))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 46 ms Beats 92.63% 
   Memory 15.1 MB Beats 98.50%

2. Runtime 52 ms Beats 87.95% 
   Memory 15.3 MB Beats 49.59%
"""

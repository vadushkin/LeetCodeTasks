class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        return max(int(word) if word.isdigit() else len(word) for word in strs)


def main():
    s = Solution()
    print(s.maximumValue(["alic3", "bob", "3", "4", "00000"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 39 ms Beats 66.86% 
   Memory 13.9 MB Beats 57.5%

2. Runtime 43 ms Beats 56.32% 
   Memory 13.8 MB Beats 96.57%
"""

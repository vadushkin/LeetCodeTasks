class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) > len(str2):
            min_str = str2
            max_str = str1
        else:
            min_str = str1
            max_str = str2

        for symbol in range(len(min_str), -1, -1):
            if (min_str[:symbol] * (len(max_str) // max(len(min_str[:symbol]), 1)) == max_str) and (
                    min_str[:symbol] * (len(min_str) // max(len(min_str[:symbol]), 1)) == min_str):
                return min_str[:symbol]

        return ""


def main():
    s = Solution()
    print(s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 38 ms Beats 61.33% 
   Memory 13.8 MB Beats 70.81%

2. Runtime 34 ms Beats 75.85%
   Memory 13.8 MB Beats 70.81%
"""

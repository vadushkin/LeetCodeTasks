class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False

            n1, n2 = len1 // k, len2 // k
            base = str1[:k]

            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]

        return ""


def main():
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 28 ms Beats 93.33% 
   Memory 13.8 MB Beats 70.81%

2. Runtime 34 ms Beats 75.85%
   Memory 13.8 MB Beats 70.81% 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        return s == '' if s == (s := s.replace('()', '').replace('{}', '').replace('[]', '')) else self.isValid(s)


def main():
    s = Solution()
    print(s.isValid("()"))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 58 ms Beats 8.64% 
   Memory 21.6 MB Beats 17.97%
 
2. Runtime 56 ms Beats 10.30% 
   Memory 21.5 MB Beats 17.97%
"""

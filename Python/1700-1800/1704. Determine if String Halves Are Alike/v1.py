class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        if n % 2 == 1:
            return False

        first_half = s[:n // 2]
        second_half = s[n // 2:]

        first_lst_vowels = [v for v in first_half if v in ['a', 'e', 'i', 'o', 'u',
                                                           'A', 'E', 'I', 'O', 'U']]
        second_lst_vowels = [v for v in second_half if v in ['a', 'e', 'i', 'o', 'u',
                                                             'A', 'E', 'I', 'O', 'U']]

        return len(first_lst_vowels) == len(second_lst_vowels)


def main():
    s = Solution()
    print(s.halvesAreAlike("AbCdEfGh"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 70 ms Beats 43.93%
   Memory 14 MB Beats 5.13%

2. Runtime 48 ms Beats 77.72%
   Memory 13.8 MB Beats 77.72%
"""

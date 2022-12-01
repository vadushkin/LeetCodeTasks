class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aioeuAIOEU')
        cnt_first_half, cnt_second_half = 0, 0

        for index in range(len(s) // 2):
            if s[index] in vowels:
                cnt_first_half += 1

            if s[-index - 1] in vowels:
                cnt_second_half += 1

        return cnt_first_half == cnt_second_half


def main():
    s = Solution()
    print(s.halvesAreAlike("helloworld"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 44 ms Beats 82.43%
   Memory 13.9 MB Beats 77.72%

2. Runtime 70 ms Beats 43.93%
   Memory 13.9 MB Beats 33.58%
"""

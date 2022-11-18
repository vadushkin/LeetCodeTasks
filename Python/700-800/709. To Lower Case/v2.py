from string import ascii_uppercase, ascii_lowercase


class Solution:
    def toLowerCase(self, s: str) -> str:

        answer = []

        for i in s:
            if i in ascii_uppercase:
                index_i = ascii_uppercase.find(i)
                answer.append(ascii_lowercase[index_i])
            else:
                answer.append(i)

        return ''.join(answer)


def main():
    s = Solution()
    print(s.toLowerCase('Cookies reaLLy gooD'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 77 ms Beats 5.68%
   Memory 13.9 MB Beats 7.98%

2. Runtime 51 ms Beats 63.87%
   Memory 13.8 MB Beats 51.74%
"""

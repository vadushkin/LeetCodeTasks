import re


class Solution:
    def countTime(self, time: str) -> int:
        pattern = time.replace('?', '.')

        return sum(
            re.fullmatch(pattern, f'{hour:02}:{minute:02}') is not None
            for hour in range(24)
            for minute in range(60)
        )


def main():
    s = Solution()
    print(s.countTime("?5:00"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 112 ms Beats 8.48% 
   Memory 13.9 MB Beats 71.2%

2. Runtime 110 ms Beats 9.19% 
   Memory 13.9 MB Beats 71.2%
"""

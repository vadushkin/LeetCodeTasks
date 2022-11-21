class Solution:
    def sumGame(self, num: str) -> bool:
        count, s, n = 0, 0, len(num)

        for i, d in enumerate(num):
            if d == '?':
                count += 1 if i < n // 2 else -1
            elif i < n // 2:
                s += int(d)
            else:
                s -= int(d)

        if s * 2 == -9 * count:
            return False
        return True


def main():
    s = Solution()
    print(s.sumGame("?019"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 594 ms Beats 12.50%
   Memory 15.1 MB Beats 23.86%

2. Runtime 296 ms Beats 59.9%
   Memory 15.1 MB Beats 23.86%
"""

class Solution:
    def maximum69Number(self, num: int) -> int:

        num = str(num)

        for i in range(len(num)):
            if num[i] == '6':
                num = num[:i] + '9' + num[i + 1:]
                break

        return int(num)


def main():
    s = Solution()
    print(s.maximum69Number(9669))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 48 ms Beats 73.11%
   Memory 13.9 MB Beats 54.69%

2. Runtime 32 ms Beats 93.8%
   Memory 13.8 MB Beats 54.69%
"""

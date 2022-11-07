class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        index_six = num.find('6')

        return int(num[:index_six] + '9' + num[index_six + 1:]) if index_six != -1 else num


def main():
    s = Solution()
    print(s.maximum69Number(9999))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 36 ms Beats 87.86%
   Memory 13.8 MB Beats 54.69%

2. Runtime 46 ms Beats 76.57%
   Memory 13.9 MB Beats 9.69%
"""

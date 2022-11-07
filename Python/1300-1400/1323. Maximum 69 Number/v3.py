class Solution:
    def maximum69Number(self, num: int) -> int:
        num_string = str(num)

        return int(num_string.replace('6', '9', 1))


def main():
    s = Solution()
    print(s.maximum69Number(9669))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 58 ms Beats 41.91%
   Memory 13.8 MB Beats 54.69%  

2. Runtime 47 ms Beats 74.92%
   Memory 13.7 MB Beats 95.47%
"""

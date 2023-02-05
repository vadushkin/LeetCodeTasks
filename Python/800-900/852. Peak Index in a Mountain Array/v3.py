class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        x1, x2 = self.gold1(left, right), self.gold2(left, right)

        while x1 < x2:
            if arr[x1] < arr[x2]:
                left = x1
                x1 = x2
                x2 = self.gold1(x1, right)
            else:
                right = x2
                x2 = x1
                x1 = self.gold2(left, x2)

        return arr.index(max(arr[left:right + 1]), left)

    @staticmethod
    def gold2(left: int, right: int) -> int:
        return left + int(round((right - left) * 0.618))

    @staticmethod
    def gold1(left: int, right: int) -> int:
        return left + int(round((right - left) * 0.382))


def main():
    s = Solution()
    print(s.peakIndexInMountainArray([0, 2, 1, 0]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 623 ms Beats 72.9% 
   Memory 27.9 MB Beats 10.20%
   
2. Runtime 647 ms Beats 46.47% 
   Memory 27.8 MB Beats 31.77%
"""

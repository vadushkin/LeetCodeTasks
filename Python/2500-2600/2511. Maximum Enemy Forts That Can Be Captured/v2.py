class Solution:
    def captureForts(self, forts: list[int]) -> int:
        return max(self.solve(forts), self.solve(forts[::-1]))

    @staticmethod
    def solve(arr):
        max_ = 0
        count, flag = 0, False

        for num in arr:

            if num == 1:
                count, flag = 0, True
            elif num == -1:
                max_, count, flag = max(max_, count), 0, False
            else:
                if flag:
                    count += 1

        return max_


def main():
    s = Solution()
    print(s.captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 40 ms Beats 59.61%
   Memory 13.8 MB Beats 66.6%

2. Runtime 47 ms Beats 18.78% 
   Memory 13.9 MB Beats 66.6%
"""

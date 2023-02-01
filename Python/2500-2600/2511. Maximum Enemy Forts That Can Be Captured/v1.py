class Solution:
    def captureForts(self, forts: list[int]) -> int:
        ans = ii = 0

        for i, x in enumerate(forts):
            if x:
                if forts[ii] == -x:
                    ans = max(ans, i - ii - 1)

                ii = i

        return ans


def main():
    s = Solution()
    print(s.captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 38 ms Beats 71.95% 
   Memory 13.8 MB Beats 66.6%

2. Runtime 30 ms Beats 98.7% 
   Memory 13.8 MB Beats 66.6%
"""

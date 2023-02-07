class Solution:
    def findLucky(self, arr: list[int]) -> int:
        cnt = [0] * 501

        for a in arr:
            cnt[a] += 1

        for i in range(500, 0, -1):
            if cnt[i] == i:
                return i

        return -1


def main():
    s = Solution()
    print(s.findLucky([2, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 54 ms Beats 91.11% 
   Memory 14 MB Beats 53.36%

2. Runtime 65 ms Beats 48.22% 
   Memory 14 MB Beats 53.36%
"""

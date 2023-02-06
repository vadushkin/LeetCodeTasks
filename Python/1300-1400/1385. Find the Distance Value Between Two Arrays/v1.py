class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
            else:
                count += 1

        return count


def main():
    s = Solution()
    print(s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 120 ms Beats 50.49% 
   Memory 14 MB Beats 74.95%

2. Runtime 107 ms Beats 62.43% 
   Memory 13.9 MB Beats 98.34%
"""

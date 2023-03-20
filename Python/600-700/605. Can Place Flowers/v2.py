class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        zeros, answer = 1, 0

        for f in flowerbed:
            if f == 0:
                zeros += 1
            else:
                answer += (zeros - 1) // 2
                zeros = 0

        return answer + zeros // 2 >= n


def main():
    s = Solution()
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 150 ms Beats 98.97% 
   Memory 14.3 MB Beats 65.78%

2. Runtime 156 ms Beats 93.87% 
   Memory 14.3 MB Beats 94.1%
"""

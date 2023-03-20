class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        return sum(
            (len(slot) - 1) // 2 for slot in ''.join(list(map(str, [0] + flowerbed + [0]))).split('1') if slot) >= n


def main():
    s = Solution()
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 171 ms Beats 51.60% 
   Memory 15.4 MB Beats 20.94%

2. Runtime 180 ms Beats 28.40% 
   Memory 15.3 MB Beats 20.94%
"""

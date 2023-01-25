class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        res = [0] * num_people
        i = 0

        while candies > 0:
            res[i % num_people] += min(candies, i + 1)
            candies -= i + 1
            i += 1

        return res


def main():
    s = Solution()
    print(s.distributeCandies(7, 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 62 ms Beats 38.14%
   Memory 14 MB Beats 9.79%

2. Runtime 52 ms Beats 48.20% 
   Memory 13.9 MB Beats 47.94%
"""

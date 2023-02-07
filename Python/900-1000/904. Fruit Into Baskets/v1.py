class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count, i = {}, 0

        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1

            if len(count) > 2:
                count[fruits[i]] -= 1

                if count[fruits[i]] == 0:
                    del count[fruits[i]]

                i += 1

        return j - i + 1


def main():
    s = Solution()
    print(s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 812 ms Beats 97.7% 
   Memory 20.1 MB Beats 80.52%

2. Runtime 883 ms Beats 85.94% 
   Memory 20.3 MB Beats 35.66%
"""

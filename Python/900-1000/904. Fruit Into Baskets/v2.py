class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        res = cur = count_b = a = b = 0

        for c in fruits:
            cur = cur + 1 if c in (a, b) else count_b + 1
            count_b = count_b + 1 if c == b else 1

            if b != c:
                a, b = b, c

            res = max(res, cur)

        return res


def main():
    s = Solution()
    print(s.totalFruit([1, 2, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 849 ms Beats 91.79% 
   Memory 20 MB Beats 80.52%

2. Runtime 807 ms Beats 97.40% 
   Memory 20.1 MB Beats 51.27%
"""

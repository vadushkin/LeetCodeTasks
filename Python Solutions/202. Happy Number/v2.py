class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


def main():
    s = Solution()
    print(s.isHappy(19))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 39.25% of Python3 online submissions for Happy Number.
Memory Usage: 14 MB, less than 15.23% of Python3 online submissions for Happy Number.

2. Runtime: 80 ms, faster than 6.60% of Python3 online submissions for Happy Number.
Memory Usage: 14 MB, less than 15.23% of Python3 online submissions for Happy Number.
"""

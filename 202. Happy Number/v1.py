class Solution:
    def isHappy(self, n: int) -> bool:
        b = []
        was_in_b = []
        while n:
            for i in str(n):
                b.append(int(i) ** 2)
            if sum(b) == int(n):
                return True
            n = sum(b)
            if int(n) in was_in_b:
                return False
            was_in_b.append(n)
            b.clear()


def main():
    s = Solution()
    print(s.isHappy(10))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 91 ms, faster than 5.06% of Python3 online submissions for Happy Number.
Memory Usage: 13.9 MB, less than 61.90% of Python3 online submissions for Happy Number.

2. Runtime: 62 ms, faster than 34.38% of Python3 online submissions for Happy Number.
Memory Usage: 13.8 MB, less than 61.90% of Python3 online submissions for Happy Number.
"""

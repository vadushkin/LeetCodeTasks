class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return ['FizzBuzz'[i % -3 & -4:i % -5 & 8 ^ 12] or str(i) for i in range(1, n + 1)]


def main():
    s = Solution()
    print(s.fizzBuzz(15))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 80 ms, faster than 38.81% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.3 MB, less than 17.67% of Python3 online submissions for Fizz Buzz.

2. Runtime: 88 ms, faster than 24.25% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.2 MB, less than 17.67% of Python3 online submissions for Fizz Buzz.
"""

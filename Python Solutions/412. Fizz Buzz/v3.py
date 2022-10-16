class Solution:
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]


def main():
    s = Solution()
    print(s.fizzBuzz(15))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 75 ms, faster than 47.84% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.1 MB, less than 43.85% of Python3 online submissions for Fizz Buzz.

2. Runtime: 86 ms, faster than 27.87% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.1 MB, less than 17.67% of Python3 online submissions for Fizz Buzz.
"""

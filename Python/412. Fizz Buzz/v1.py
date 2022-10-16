class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


def main():
    s = Solution()
    print(s.fizzBuzz(15))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 102 ms, faster than 6.07% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15 MB, less than 85.42% of Python3 online submissions for Fizz Buzz.

2. Runtime: 84 ms, faster than 31.46% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15 MB, less than 43.85% of Python3 online submissions for Fizz Buzz.
"""

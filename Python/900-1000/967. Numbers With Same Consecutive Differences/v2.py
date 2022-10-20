class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:

        if n == 1:
            return [i for i in range(10)]

        queue = [digit for digit in range(1, 10)]

        for level in range(n - 1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                next_digits = {tail_digit + k, tail_digit - k}

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            queue = next_queue

        return queue


def main():
    s = Solution()
    print(s.numsSameConsecDiff(3, 7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 80 ms, faster than 27.21% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.1 MB, less than 73.81% of Python3 online submissions for Numbers With Same Consecutive Differences.

2. Runtime: 103 ms, faster than 6.12% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.2 MB, less than 41.16% of Python3 online submissions for Numbers With Same Consecutive Differences.
"""

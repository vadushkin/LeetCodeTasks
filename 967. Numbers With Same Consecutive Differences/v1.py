class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:

        if n == 1:
            return [i for i in range(10)]

        ans = []

        def DFS(n, num):
            if n == 0:
                return ans.append(num)

            tail_digit = num % 10
            next_digits = {tail_digit + k, tail_digit - k}

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(n - 1, new_num)

        for num in range(1, 10):
            DFS(n - 1, num)

        return list(ans)


def main():
    s = Solution()
    print(s.numsSameConsecDiff(3, 7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 70 ms, faster than 43.88% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.2 MB, less than 73.81% of Python3 online submissions for Numbers With Same Consecutive Differences.

2. Runtime: 74 ms, faster than 34.69% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.3 MB, less than 21.77% of Python3 online submissions for Numbers With Same Consecutive Differences.
"""

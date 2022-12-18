class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        if len(temperatures) <= 1:
            return [0]

        stack = [len(temperatures) - 1]
        ans = [0]

        for pos in range(len(temperatures) - 2, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[pos]:
                stack.pop()

            if len(stack) == 0:
                ans.append(0)
            else:
                ans.append(stack[-1] - pos)

            stack.append(pos)

        ans.reverse()
        return ans


def main():
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 4426 ms Beats 6.58%
   Memory 29.1 MB Beats 42.44%

2. Runtime 4307 ms Beats 7.92%
   Memory 29 MB Beats 42.44%
"""

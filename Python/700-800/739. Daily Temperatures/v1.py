class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        answer = []

        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                answer.append(0)
                break

            for j in range(i + 1, len(temperatures) + 1):
                if j == len(temperatures):
                    answer.append(0)
                    break

                if temperatures[i] < temperatures[j]:
                    answer.append(j - i)
                    break

        return answer


def main():
    s = Solution()
    print(s.dailyTemperatures([30, 40, 50, 60]))


if __name__ == "__main__":
    main()

"""Tests:
1. Time Limit Exceeded
   31 / 48 testcases passed

2. Time Limit Exceeded
   31 / 48 testcases passed
"""

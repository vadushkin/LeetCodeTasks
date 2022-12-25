import bisect


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:

        nums.sort()

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        answer = []

        for query in queries:
            index = bisect.bisect_right(nums, query)
            answer.append(index)

        return answer


def main():
    s = Solution()
    print(s.answerQueries([1, 2, 4, 5], [1, 5, 19]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 103 ms Beats 96.80%
   Memory 14.2 MB Beats 40.29%

2. Runtime 104 ms Beats 96.31%
   Memory 14.2 MB Beats 40.29%
"""

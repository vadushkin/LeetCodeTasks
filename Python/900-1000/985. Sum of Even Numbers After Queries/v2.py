class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        amount = sum(x for x in nums if x % 2 == 0)
        ans = []

        for x, k in queries:
            if nums[k] % 2 == 0:
                amount -= nums[k]
            nums[k] += x
            if nums[k] % 2 == 0:
                amount += nums[k]
            ans.append(amount)

        return ans


def main():
    s = Solution()
    print(s.sumEvenAfterQueries([1, 2, 3, 4], [[3, 0], [-2, 1], [-2, 2], [1, 3]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1079 ms, faster than 26.28% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.3 MB, less than 97.19% of Python3 online submissions for Sum of Even Numbers After Queries.

2. Runtime: 1225 ms, faster than 15.31% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.4 MB, less than 97.19% of Python3 online submissions for Sum of Even Numbers After Queries.
"""

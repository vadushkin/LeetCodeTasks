class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        ans = [0] * len(queries)
        s = sum(num for num in nums if not num % 2)
        for i, (v_add, j) in enumerate(queries):
            old, nums[j] = nums[j], nums[j] + v_add
            s += nums[j] * (~nums[j] % 2) - old * (~old % 2)
            ans[i] = s
        return ans


def main():
    s = Solution()
    print(s.sumEvenAfterQueries([1, 2, 3, 4], [[3, 0], [-2, 1], [-2, 2], [1, 3]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 541 ms, faster than 90.82% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.6 MB, less than 43.88% of Python3 online submissions for Sum of Even Numbers After Queries.

2. Runtime: 1111 ms, faster than 25.51% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.6 MB, less than 20.41% of Python3 online submissions for Sum of Even Numbers After Queries.
"""

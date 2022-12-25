class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:

        nums.sort()
        ans = []

        for query in queries:
            count = 0

            for num in nums:
                if query >= num:
                    query -= num
                    count += 1
                else:
                    break

            ans.append(count)

        return ans


def main():
    s = Solution()
    print(s.answerQueries([4, 5, 2, 1], [3, 10, 21]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 309 ms Beats 54.85% 
   Memory 14.1 MB Beats 79.61%

2. Runtime 326 ms Beats 51.75%
   Memory 14.1 MB Beats 79.61%
"""

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        d = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        return [x for x in d if d[x] == min(d.values())]


def main():
    s = Solution()
    print(s.findRestaurant(['2', '3', '4', '5', '1'], ['1', '6', '3', '4', '5', '3']))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 681 ms, faster than 20.59% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 14.6 MB, less than 6.82% of Python3 online submissions for Minimum Index Sum of Two Lists.

2. Runtime: 637 ms, faster than 22.43% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 14.5 MB, less than 6.82% of Python3 online submissions for Minimum Index Sum of Two Lists.
"""

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hashmap = {}
        for i in range(len(list1)):
            hashmap[list1[i]] = i

        res = []
        min_sum = float("inf")

        for j in range(len(list2)):
            if list2[j] in hashmap:
                Sum = j + hashmap[list2[j]]

                if Sum < min_sum:
                    min_sum = Sum
                    res = [list2[j]]
                elif Sum == min_sum:
                    res.append(list2[j])
        return res


def main():
    s = Solution()
    print(s.findRestaurant(['1', '2', '3', '4', '5', '6'], ['4', '3', '1', '5', '2']))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 417 ms, faster than 39.04% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 14.4 MB, less than 40.00% of Python3 online submissions for Minimum Index Sum of Two Lists.

2. Runtime: 221 ms, faster than 80.67% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 14.5 MB, less than 40.00% of Python3 online submissions for Minimum Index Sum of Two Lists.
"""

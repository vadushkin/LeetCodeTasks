class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count_lst = [arr.count(n) for n in set(arr)]
        return len(count_lst) == len(set(count_lst))


def main():
    s = Solution()
    print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 123 ms Beats 5.3%
   Memory 13.9 MB Beats 72.74%

2. Runtime 75 ms Beats 33.33%
   Memory 13.9 MB Beats 72.74%
"""

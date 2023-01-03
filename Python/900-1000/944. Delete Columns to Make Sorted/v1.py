class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))


def main():
    s = Solution()
    print(s.minDeletionSize(["cba", "daf", "ghi"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 81 ms Beats 99.16%
   Memory 14.8 MB Beats 25.26%
 
2. Runtime 183 ms Beats 71.37%
   Memory 14.8 MB Beats 25.26%
"""

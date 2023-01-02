class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if '+' in x else -1 for x in operations)


def main():
    s = Solution()
    print(s.finalValueAfterOperations(['--X', '++X', '--X']))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 60 ms Beats 69.73%
   Memory 13.9 MB Beats 54.42%

2. Runtime 52 ms Beats 90.2%
   Memory 13.9 MB Beats 10.92%
"""

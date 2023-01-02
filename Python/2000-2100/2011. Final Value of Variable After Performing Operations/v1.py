class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        answer = 0

        for operation in operations:
            if operation[0] == '-' or operation[-1] == '-':
                answer -= 1
            else:
                answer += 1

        return answer


def main():
    s = Solution()
    print(s.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 47 ms Beats 97.7%
   Memory 13.9 MB Beats 54.42%

2. Runtime 53 ms Beats 86.80%
   Memory 13.9 MB Beats 54.42%
"""

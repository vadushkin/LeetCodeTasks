class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()

            else:
                stack.append(char)

        return ''.join(stack)


def main():
    s = Solution()
    print(s.removeDuplicates("abbaca"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 221 ms Beats 35.53%
   Memory 15 MB Beats 18.64%

2. Runtime 133 ms Beats 75.75%
   Memory 14.8 MB Beats 86.70%
"""

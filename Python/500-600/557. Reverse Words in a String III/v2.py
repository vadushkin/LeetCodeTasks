class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


def main():
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 39 ms, faster than 91.92% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.5 MB, less than 82.00% of Python3 online submissions for Reverse Words in a String III.

2. Runtime: 58 ms, faster than 66.20% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.5 MB, less than 82.00% of Python3 online submissions for Reverse Words in a String III.
"""

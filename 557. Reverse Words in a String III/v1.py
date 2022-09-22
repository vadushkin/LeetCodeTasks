class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])


def main():
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 75 ms, faster than 42.55% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.6 MB, less than 82.00% of Python3 online submissions for Reverse Words in a String III.

2. Runtime: 68 ms, faster than 50.73% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.6 MB, less than 46.10% of Python3 online submissions for Reverse Words in a String III.
"""

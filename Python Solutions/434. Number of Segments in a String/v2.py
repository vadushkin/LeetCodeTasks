class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count


def main():
    s = Solution()
    print(s.countSegments("Salutation, "))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 53 ms, faster than 45.08% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.8 MB, less than 94.80% of Python3 online submissions for Number of Segments in a String.

2. Runtime: 26 ms, faster than 97.49% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.8 MB, less than 49.05% of Python3 online submissions for Number of Segments in a String.
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        head = len(s) % k
        grouping = []

        if head:
            grouping.append(s[:head])

        for index in range(head, len(s), k):
            grouping.append(s[index: index + k])

        return '-'.join(grouping).upper()


def main():
    s = Solution()
    print(s.licenseKeyFormatting("2-5G-3J", 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 61 ms, faster than 85.04% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.6 MB, less than 59.08% of Python3 online submissions for License Key Formatting.

2. Runtime: 61 ms, faster than 85.04% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.6 MB, less than 59.08% of Python3 online submissions for License Key Formatting.
"""

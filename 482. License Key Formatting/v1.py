class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = (s.upper()).replace("-", "")[::-1]
        ans = str()
        for i in range(0, len(s), k):
            ans += s[i:i + k] + "-"
        return ans[::-1][1:]


def main():
    s = Solution()
    print(s.licenseKeyFormatting("2-5g-3-J", 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 43 ms, faster than 96.39% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.3 MB, less than 86.89% of Python3 online submissions for License Key Formatting.

2. Runtime: 75 ms, faster than 70.55% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.3 MB, less than 97.73% of Python3 online submissions for License Key Formatting.
"""

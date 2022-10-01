class Solution:
    def numDecodings(self, s: str) -> int:
        one = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
        two = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1,
               '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2,
               '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}
        dp = 1, one.get(s[:1], 0)
        for i in range(1, len(s)):
            dp = dp[1], (one.get(s[i], 0) * dp[1] + two.get(s[i - 1: i + 1], 0) * dp[0]) % 1000000007

        return dp[-1]


def main():
    s = Solution()
    print(s.numDecodings("1*"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1312 ms, faster than 39.93% of Python3 online submissions for Decode Ways II.
Memory Usage: 15 MB, less than 79.86% of Python3 online submissions for Decode Ways II.

2. Runtime: 1316 ms, faster than 39.93% of Python3 online submissions for Decode Ways II.
Memory Usage: 15 MB, less than 93.17% of Python3 online submissions for Decode Ways II.
"""

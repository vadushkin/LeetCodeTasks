class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s)):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return ''.join(sorted(s))


def main():
    s = Solution()
    print(s.orderlyQueue("oak", 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime N/A (19 ms)
   Beats N/A (13.7 mb)
    
2. Runtime N/A (25 ms)
   Beats N/A (13.7 mb)
"""

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return ''.join(sorted(s))


def main():
    s = Solution()
    print(s.orderlyQueue("nhtq", 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 30 ms Beats 97.62%
   Memory 13.9 MB Beats 72.62%
   
2. Runtime 65 ms Beats 38.9%
   Memory 13.9 MB Beats 39.29%
"""

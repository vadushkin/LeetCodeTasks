class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = pattern
        t = s.split()
        return len(set(zip(p, t))) == len(set(p)) == len(set(t)) and len(p) == len(t)


def main():
    s = Solution()
    print(s.wordPattern("dabba", "dog cat cat s dog"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 49.20% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 24.20% of Python3 online submissions for Word Pattern.

2. Runtime: 37 ms, faster than 80.36% of Python3 online submissions for Word Pattern.
Memory Usage: 13.8 MB, less than 73.78% of Python3 online submissions for Word Pattern.
"""

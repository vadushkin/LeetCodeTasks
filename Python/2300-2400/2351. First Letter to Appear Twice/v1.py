class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s_set = set()
        for x in s:
            if x in s_set:
                return x
            else:
                s_set.add(x)


def main():
    s = Solution()
    print(s.repeatedCharacter("jkodgypoya"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 42 ms, faster than 68.60% of Python3 online submissions for First Letter to Appear Twice.
Memory Usage: 13.9 MB, less than 7.43% of Python3 online submissions for First Letter to Appear Twice.

2. Runtime: 34 ms, faster than 87.50% of Python3 online submissions for First Letter to Appear Twice.
Memory Usage: 14 MB, less than 7.43% of Python3 online submissions for First Letter to Appear Twice.
"""

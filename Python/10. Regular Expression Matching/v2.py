class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not (1 <= len(s) <= 20):
            return False
        if not (1 <= len(p) <= 30):
            return False
        if len(s) != len(p):
            return False
        if s == p:
            return True
        last_s = ''
        last_p = ''
        for i in range(len(s)):
            if s[i] == p[i]:
                continue
            if s[i] == '.':
                continue
            if p[i] == '.':
                continue
            if s[i] == '*':
                if not last_s:
                    last_s = s[i - 1]
                if last_s == p[i] or last_s == '.':
                    continue
                return False
            if p[i] == '*':
                if not last_p:
                    last_p = p[i - 1]
                if last_p == s[i] or last_p == '.':
                    continue
                return False
            return False
        return True


s = Solution()
print(s.isMatch("a***", "a*.*"))

# why
# "aab" == "c*a*b" -> True?????
# okay, re.search(f"^{p}$", s) is not None

"""Tests:
1. Fastest

2. Fastest
"""

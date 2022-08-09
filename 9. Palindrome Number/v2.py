class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == ''.join(reversed(str(x))):
            return True
        return False

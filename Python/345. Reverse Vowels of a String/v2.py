class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU'
        while left < right:
            if s[left] in m and s[right] in m:

                s[left], s[right] = s[right], s[left]

                left += 1
                right -= 1

            elif s[left] not in m:
                left += 1

            elif s[right] not in m:
                right -= 1

        return ''.join(s)


def main():
    s = Solution()
    print(s.reverseVowels("helloooooowlse"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 95.95% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15 MB, less than 57.94% of Python3 online submissions for Reverse Vowels of a String.

2. Runtime: 72 ms, faster than 79.41% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15.1 MB, less than 57.94% of Python3 online submissions for Reverse Vowels of a String.
"""

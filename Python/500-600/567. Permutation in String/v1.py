class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = [ord(x) - ord('a') for x in s1]
        s2 = [ord(x) - ord('a') for x in s2]

        target = [0] * 26

        for x in s1:
            target[x] += 1

        window = [0] * 26

        for i, x in enumerate(s2):
            window[x] += 1

            if i >= len(s1):
                window[s2[i - len(s1)]] -= 1

            if window == target:
                return True

        return False


def main():
    s = Solution()
    print(s.checkInclusion("ab", "eidbaoo"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 71 ms Beats 81.14% 
   Memory 14.1 MB Beats 28.54%

2. Runtime 72 ms Beats 79.73% 
   Memory 14.3 MB Beats 7.27%
"""

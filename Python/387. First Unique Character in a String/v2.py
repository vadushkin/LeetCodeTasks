import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


def main():
    s = Solution()
    print(s.firstUniqChar("leetcode"))


if __name__ == "__main__":
    main()

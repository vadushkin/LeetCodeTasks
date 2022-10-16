class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == turnedOn]


def main():
    s = Solution()
    print(s.readBinaryWatch(1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 73 ms, faster than 13.14% of Python3 online submissions for Binary Watch.
Memory Usage: 13.9 MB, less than 30.79% of Python3 online submissions for Binary Watch.

2. Runtime: 68 ms, faster than 21.28% of Python3 online submissions for Binary Watch.
Memory Usage: 13.9 MB, less than 30.79% of Python3 online submissions for Binary Watch.
"""

class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        sequence = []
        for d in data:
            sequence.append("{0:08b}".format(d))
        i = 0
        n = len(sequence)
        while i < n:
            if sequence[i][0] == '0':
                i += 1
                continue
            if sequence[i][:3] == '110' and n - i >= 1:
                if sequence[i + 1][:2] == '10':
                    i += 2
                    continue
            if sequence[i][:4] == '1110' and n - i >= 2:
                if sequence[i + 1][:2] == '10' and sequence[i + 2][:2] == '10':
                    i += 3
                    continue
            if sequence[i][:5] == '11110' and n - i >= 3:
                if sequence[i + 1][:2] == '10' and sequence[i + 2][:2] == '10' and sequence[i + 3][:2] == '10':
                    i += 4
                    continue
            else:
                return False
        return True


def main():
    s = Solution()
    print(s.validUtf8([197, 130, 1, 105, 302, 513]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 297 ms, faster than 9.79% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 15 MB, less than 12.72% of Python3 online submissions for UTF-8 Validation.

2. Runtime: 308 ms, faster than 8.19% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 15 MB, less than 12.72% of Python3 online submissions for UTF-8 Validation.
"""

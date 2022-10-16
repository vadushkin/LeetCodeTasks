class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        n_bytes = 0
        for num in data:
            bin_rep = format(num, '#010b')[-8:]
            if n_bytes == 0:
                for bit in bin_rep:
                    if bit == '0':
                        break
                    n_bytes += 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False
            n_bytes -= 1
        return n_bytes == 0


def main():
    s = Solution()
    print(s.validUtf8([197, 130, 1, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 279 ms, faster than 13.30% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 14.1 MB, less than 70.76% of Python3 online submissions for UTF-8 Validation.

2. Runtime: 164 ms, faster than 66.23% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 14.1 MB, less than 70.76% of Python3 online submissions for UTF-8 Validation.
"""

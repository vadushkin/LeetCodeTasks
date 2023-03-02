class Solution:
    def compress(self, chars: list[str]) -> int:
        length = len(chars)

        if length < 2:
            return length

        anchor = 0
        write = 0

        for pos, char in enumerate(chars):
            if (pos + 1) == length or char != chars[pos + 1]:
                chars[write] = char
                write += 1

                if pos > anchor:
                    repeated_times = pos - anchor + 1

                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1

                anchor = pos + 1

        return write


def main():
    s = Solution()
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 66 ms Beats 39.25% 
   Memory 13.9 MB Beats 65.1%

2. Runtime 64 ms Beats 51.18% 
   Memory 13.9 MB Beats 65.1%
"""

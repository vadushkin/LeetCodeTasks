class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        
        count = 0
        direction = 1
        answer = [''] * num_rows

        for string in s:
            answer[count] += string

            if count == num_rows - 1:
                direction = -1
            if count == 0:
                direction = 1

            count += direction

        return "".join(answer)


def main():
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 50 ms Beats 94.43% 
   Memory 13.9 MB Beats 72.54%

2. Runtime 42 ms Beats 99.24% 
   Memory 14 MB Beats 72.54%
"""

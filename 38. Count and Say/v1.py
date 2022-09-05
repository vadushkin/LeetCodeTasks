class Solution:
    def countAndSay(self, n: int) -> str:
        current_string = '1'
        for _ in range(n - 1):
            next_string = ''
            j = 0
            k = 0
            while j < len(current_string):
                while (k < len(current_string) and
                       current_string[k] == current_string[j]):
                    k += 1
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string
        return current_string


def main():
    s = Solution()
    print(s.countAndSay(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 126 ms, faster than 5.30% of Python3 online submissions for Count and Say.
Memory Usage: 13.8 MB, less than 86.18% of Python3 online submissions for Count and Say.

2. Runtime: 127 ms, faster than 5.30% of Python3 online submissions for Count and Say.
Memory Usage: 13.9 MB, less than 86.18% of Python3 online submissions for Count and Say.
"""

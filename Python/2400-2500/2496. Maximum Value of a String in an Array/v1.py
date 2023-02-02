class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        answer = 0

        for alphanumeric_string in strs:
            try:
                value = int(alphanumeric_string)
            except ValueError:
                value = len(alphanumeric_string)

            answer = max(answer, value)

        return answer


def main():
    s = Solution()
    print(s.maximumValue(["alic3", "bob", "3", "4", "00000"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 36 ms Beats 76.52%
   Memory 13.8 MB Beats 96.57%

2. Runtime 34 ms Beats 83.43% 
   Memory 13.8 MB Beats 96.57%
"""

class Solution:
    def maxLength(self, arr: list[str]) -> int:

        uniq_elements = ['']
        maximum = 0

        for i in range(len(arr)):
            sz = len(uniq_elements)

            for j in range(sz):
                x = arr[i] + uniq_elements[j]

                if len(x) == len(set(x)):
                    uniq_elements.append(x)
                    maximum = max(maximum, len(x))

        return maximum


def main():
    s = Solution()
    print(s.maxLength(["aa", "bb"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 65 ms, faster than 99.51% of Python3 online submissions for Maximum 
Length of a Concatenated String with Unique Characters.
Memory Usage: 18.5 MB, less than 24.57% of Python3 online submissions for Maximum 
Length of a Concatenated String with Unique Characters.

2. Runtime: 127 ms, faster than 83.48% of Python3 online submissions for Maximum 
Length of a Concatenated String with Unique Characters.
Memory Usage: 18.5 MB, less than 24.57% of Python3 online submissions for Maximum 
Length of a Concatenated String with Unique Characters.
"""

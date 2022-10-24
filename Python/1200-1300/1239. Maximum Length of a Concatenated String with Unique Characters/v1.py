class Solution:
    def maxLength(self, arr: list[str]) -> int:

        dp = [set()]

        for a in arr:

            if len(set(a)) < len(a):
                continue

            a = set(a)

            for c in dp[:]:
                if a & c:
                    continue

                dp.append(a | c)

        return max(len(a) for a in dp)


def main():
    s = Solution()
    print(s.maxLength(["aa", "bb"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 155 ms, faster than 76.65% of Python3 online submissions for Maximum 
Length of a Concatenated String with Unique Characters.
Memory Usage: 55.5 MB, less than 5.04% of Python3 online submissions for Maximum 
Length of a Concatenated String with Unique Characters.

2. Runtime: 201 ms, faster than 59.56% of Python3 online submissions for Maximum
Length of a Concatenated String with Unique Characters.
Memory Usage: 55.5 MB, less than 5.04% of Python3 online submissions for Maximum
Length of a Concatenated String with Unique Characters.
"""

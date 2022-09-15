from collections import deque


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        changed.sort()
        stk, res = deque([]), []
        for i in changed:
            if stk and stk[0] * 2 == i:
                b = stk.popleft()
                res.append(b)
            else:
                stk.append(i)
        return res if not stk else []


def main():
    s = Solution()
    print(s.findOriginalArray([1, 2, 3, 4, 6, 8]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 3162 ms, faster than 16.26% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 29 MB, less than 97.66% of Python3 online submissions for Find Original Array From Doubled Array.

2. Runtime: 3220 ms, faster than 15.09% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 29 MB, less than 98.24% of Python3 online submissions for Find Original Array From Doubled Array.
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        out = []

        for i in sorted(intervals, key=lambda j: j[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += [i]

        return out


def main():
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 144 ms Beats 89.16% 
   Memory 18 MB Beats 78.23%

2. Runtime 154 ms Beats 57.59% 
   Memory 18.1 MB Beats 48.6%
"""

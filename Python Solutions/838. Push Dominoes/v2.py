class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = 'L' + dominoes + 'R'
        res = ""
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.':
                continue
            middle = j - i - 1
            if i:
                res += d[i]
            if d[i] == d[j]:
                res += d[i] * middle
            elif d[i] == 'L' and d[j] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2)
            i = j
        return res


def main():
    s = Solution()
    print(s.pushDominoes(".L.R...LR..L.."))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 208 ms, faster than 98.83% of Python3 online submissions for Push Dominoes.
Memory Usage: 15.4 MB, less than 95.79% of Python3 online submissions for Push Dominoes.

2. Runtime: 497 ms, faster than 58.88% of Python3 online submissions for Push Dominoes.
Memory Usage: 15.5 MB, less than 92.52% of Python3 online submissions for Push Dominoes.
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N
        f = 0

        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f
        f = 0

        for i in range(N - 1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L'
                       for f in force)


def main():
    s = Solution()
    print(s.pushDominoes(".L.R...LR..L.."))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1220 ms, faster than 18.47% of Python3 online submissions for Push Dominoes.
Memory Usage: 19.3 MB, less than 41.59% of Python3 online submissions for Push Dominoes.

2. Runtime: 442 ms, faster than 69.16% of Python3 online submissions for Push Dominoes.
Memory Usage: 19.8 MB, less than 34.11% of Python3 online submissions for Push Dominoes.
"""

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        unionFind = {}

        def find(x):
            unionFind.setdefault(x, x)
            if x != unionFind[x]:
                unionFind[x] = find(unionFind[x])
            return unionFind[x]

        def union(x, y):
            unionFind[find(x)] = find(y)

        for e in equations:
            if e[1] == '=':
                union(e[0], e[-1])
        for e in equations:
            if e[1] == '!':
                if find(e[0]) == find(e[-1]):
                    return False
        return True


def main():
    s = Solution()
    print(s.equationsPossible(["b==b", "a==a"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 100 ms, faster than 17.51% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.2 MB, less than 9.11% of Python3 online submissions for Satisfiability of Equality Equations.

2. Runtime: 112 ms, faster than 7.69% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14 MB, less than 93.85% of Python3 online submissions for Satisfiability of Equality Equations.
"""

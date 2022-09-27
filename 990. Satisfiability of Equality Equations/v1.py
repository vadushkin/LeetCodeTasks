class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent, diff = {}, []

        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])

        for s in equations:
            a, b = s[0], s[3]
            if s[1] == "=":
                x, y = find(a), find(b)
                if x != y:
                    parent[y] = x
            else:
                diff.append((a, b))
        return all(find(a) != find(b) for a, b in diff)


def main():
    s = Solution()
    print(s.equationsPossible(["a==b", "b!=a"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 94 ms, faster than 27.34% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.1 MB, less than 34.67% of Python3 online submissions for Satisfiability of Equality Equations.

2. Runtime: 48 ms, faster than 93.73% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.2 MB, less than 9.11% of Python3 online submissions for Satisfiability of Equality Equations.
"""

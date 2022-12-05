class Solution:
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i

            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)


def main():
    s = Solution()
    print(s.isIsomorphic("egg", "plant"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 85 ms Beats 46.81%
   Memory 16.6 MB Beats 5.2%

2. Runtime 71 ms Beats 66.23%
   Memory 16.5 MB Beats 5.2%
"""

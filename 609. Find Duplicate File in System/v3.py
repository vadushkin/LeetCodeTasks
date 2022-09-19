from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        m = defaultdict(list)
        for p in paths:
            path = p.split()
            directoryPath, rest = path[0], path[1:]
            for f in rest:
                fileName, fileContent = f.split('(')[0], f.split('(')[1][:-1]
                m[fileContent].append("{}/{}".format(directoryPath, fileName))
        return [m[k] for k in m.keys() if len(m[k]) > 1]


def main():
    s = Solution()
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 106 ms, faster than 85.59% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24.1 MB, less than 24.41% of Python3 online submissions for Find Duplicate File in System.

2. Runtime: 262 ms, faster than 9.15% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24 MB, less than 67.80% of Python3 online submissions for Find Duplicate File in System.
"""

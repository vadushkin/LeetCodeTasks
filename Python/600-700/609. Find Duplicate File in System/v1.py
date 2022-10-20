import re
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        dictionary = defaultdict(list)

        for j in paths:
            split_j = j.split()
            for h in split_j[1:]:
                value = re.findall(r'\(.+\)', h)[0][1:-1]
                name_file = str(split_j[0]) + '/' + h.split('(')[0]
                dictionary[value].append(name_file)

        return [i[1] for i in dictionary.items() if len(i[1]) > 1]


def main():
    s = Solution()
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 200 ms, faster than 23.56% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24.1 MB, less than 54.58% of Python3 online submissions for Find Duplicate File in System.

2. Runtime: 228 ms, faster than 14.91% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 26 MB, less than 5.93% of Python3 online submissions for Find Duplicate File in System.
"""

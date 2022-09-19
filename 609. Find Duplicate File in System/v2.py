from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        hm = defaultdict(list)
        for path in paths:
            dir_and_files = path.split()
            directory, files_and_content = dir_and_files[0], dir_and_files[1:]
            for file_and_content in files_and_content:
                filename, content = file_and_content.split('(')
                hm[content].append('/'.join([directory, filename]))
        return [val for val in hm.values() if len(val) > 1]


def main():
    s = Solution()
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 167 ms, faster than 40.51% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24 MB, less than 54.58% of Python3 online submissions for Find Duplicate File in System.

2. Runtime: 199 ms, faster than 23.90% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24.1 MB, less than 54.58% of Python3 online submissions for Find Duplicate File in System.
"""

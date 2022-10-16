class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split(" ")
        str_list = list(filter(None, st))
        x = str_list[-1]
        return (len(x))


s = Solution()
print(s.lengthOfLastWord("asdasd asdadas asdasd"))

"""Tests:
1. Runtime: 47 ms, faster than 50.73% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.8 MB, less than 80.51% of Python3 online submissions for Length of Last Word.

2. Runtime: 71 ms, faster than 5.78% of Python3 online submissions for Length of Last Word. O_O
Memory Usage: 13.8 MB, less than 80.51% of Python3 online submissions for Length of Last Word.

3. Runtime: 53 ms, faster than 32.77% of Python3 online submissions for Length of Last Word.
Memory Usage: 14 MB, less than 5.32% of Python3 online submissions for Length of Last Word. 
"""
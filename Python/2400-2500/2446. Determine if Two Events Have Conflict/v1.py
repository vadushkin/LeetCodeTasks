class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        return int(event1[1].replace(":", "")) >= int(event2[0].replace(":", "")) and int(
            event1[0].replace(":", "")) <= int(event2[1].replace(":", ""))


def main():
    s = Solution()
    print(s.haveConflict(["01:15", "02:00"], ["02:00", "03:00"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 27 ms Beats 93.56% 
   Memory 13.9 MB Beats 61.26%
   
2. Runtime 33 ms Beats 74.75% 
   Memory 13.8 MB Beats 61.26%
"""

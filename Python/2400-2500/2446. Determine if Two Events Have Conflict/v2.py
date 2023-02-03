class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        return event1[0] <= event2[1] and event2[0] <= event1[1]


def main():
    s = Solution()
    print(s.haveConflict(["01:15", "02:00"], ["02:00", "03:00"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 36 ms Beats 56.81% 
   Memory 13.8 MB Beats 96.78%
   
2. Runtime 33 ms Beats 74.75% 
   Memory 13.9 MB Beats 61.26%
"""

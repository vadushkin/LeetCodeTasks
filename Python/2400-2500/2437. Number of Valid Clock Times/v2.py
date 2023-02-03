class Solution:
    def countTime(self, time: str) -> int:
        t = 1

        if time[3] == "?":
            t *= 6

        if time[4] == "?":
            t *= 10

        if time[0:2] == "??":
            t *= 24
        elif time[0] == "?" and time[1] != "?":
            t *= 2 if time[1] in ["4", "5", "6", "7", "8", "9"] else 3
        elif time[1] == "?" and time[0] != "?":
            t *= 10 if time[0] in ["0", "1"] else 4

        return t


def main():
    s = Solution()
    print(s.countTime("?5:00"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 33 ms Beats 66.8% 
   Memory 13.9 MB Beats 17.67%
   
2. Runtime 32 ms Beats 71.38% 
   Memory 13.9 MB Beats 71.2%
"""

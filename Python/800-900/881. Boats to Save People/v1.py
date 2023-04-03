class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        lo = 0
        hi = len(people) - 1

        boats = 0

        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1

            boats += 1

        return boats


def main():
    s = Solution()
    print(s.numRescueBoats([1, 2], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 450 ms Beats 89.71% 
   Memory 20.8 MB Beats 60.46%

2. Runtime 444 ms Beats 96.67% 
   Memory 20.9 MB Beats 18.19%
"""

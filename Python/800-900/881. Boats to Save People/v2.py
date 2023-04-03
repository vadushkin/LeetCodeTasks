class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(reverse=True)

        i = 0
        j = len(people) - 1

        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1

            i += 1

        return i


def main():
    s = Solution()
    print(s.numRescueBoats([1, 2], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 459 ms Beats 71.16% 
   Memory 20.8 MB Beats 60.46%

2. Runtime 435 ms Beats 99.70% 
   Memory 20.8 MB Beats 60.46%
"""

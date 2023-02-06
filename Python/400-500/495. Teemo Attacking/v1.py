class Solution:
    def findPoisonedDuration(self, time_series: list[float | int], duration: int) -> int:
        """Logic:
        data:

        * days - [1, 2, 3, 4, 5]
        * duration - 5

        first = 1  - (days[0])
        start = False
        counts_effect_of_poison = []

        1. [(1), 2, 3, 4, 5, inf]

        if 1 + duration(5) >= 2:
            start = True
            first = first

        2. [1, (2), 3, 4, 5, inf]

        if 2 + duration(5) >= 3:
            start = True
            first = first

        3. [1, 2, (3), 4, 5, inf]

        if 3 + duration(5) >= 4:
            start = True
            first = first

        4. [1, 2, 3, (4), 5, inf]

        if 4 + duration(5) >= 5:
            start = True
            first = first

        5. [1, 2, 3, 4, (5), inf]

        if 5 + duration(5) >= inf:
            start = False
            first = days[i + 1] = (inf) Or next number
            counts_effect_of_poison.append(5 - 1 + duration(5))
                                           5 is day now
                                           1 is first day

                                     |  |  |  |  and + | * duration
            counts...poison.append( [1, 2, 3, 4, 5, inf] )

        counts_effect_of_poison: [9]

        return sum([9])
        """

        counts_effect_of_poison = []

        time_series = time_series + [float("inf")]  # for the last loop when "i" will be the IndexError :D

        first = time_series[0]

        start = False

        for i in range(len(time_series) - 1):
            if not start:
                first = time_series[i]

            if time_series[i] + duration >= time_series[i + 1]:
                start = True
            else:
                start = False
                counts_effect_of_poison.append(time_series[i] - first + duration)

        return sum(counts_effect_of_poison)


def main():
    s = Solution()
    print(s.findPoisonedDuration([1, 2, 3, 4, 5], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 268 ms Beats 68.37% 
   Memory 15.5 MB Beats 38.49%

2. Runtime 273 ms Beats 59.87% 
   Memory 15.4 MB Beats 87.35%
"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        max_weight = max(sum(weights) // days, max(weights))

        while True:
            our_days = 0
            index = 0

            while index != len(weights):
                current_weight = max_weight

                while index != len(weights) and weights[index] <= current_weight:
                    current_weight -= weights[index]
                    index += 1

                our_days += 1

            if our_days <= days:
                break
            else:
                max_weight += 1

        return max_weight


def main():
    s = Solution()
    print(s.shipWithinDays([1, 2, 3, 1, 1], 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 6108 ms Beats 5.13% 
   Memory 17 MB Beats 78.6%

2. Runtime 6065 ms Beats 5.13% 
   Memory 17 MB Beats 97.85%
"""

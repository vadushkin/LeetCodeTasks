class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        minimum_weight_capacity, maximum_weight_capacity = max(weights), sum(weights)

        while minimum_weight_capacity < maximum_weight_capacity:
            weight_capacity_of_the_ship = (minimum_weight_capacity + maximum_weight_capacity) // 2
            need_days = 1
            current_weight_for_day = 0

            for weight in weights:
                if current_weight_for_day + weight > weight_capacity_of_the_ship:
                    need_days += 1
                    current_weight_for_day = 0

                current_weight_for_day += weight

            if need_days > days:
                minimum_weight_capacity = weight_capacity_of_the_ship + 1
            else:
                maximum_weight_capacity = weight_capacity_of_the_ship

        return minimum_weight_capacity


def main():
    s = Solution()
    print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 600 ms Beats 34.67% 
   Memory 17 MB Beats 78.6%

2. Runtime 647 ms Beats 30.73% 
   Memory 17 MB Beats 97.85%
"""

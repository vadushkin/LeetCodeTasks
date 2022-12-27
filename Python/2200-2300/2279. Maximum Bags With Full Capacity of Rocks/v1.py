class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        remaining_capacity = [cap - rock for cap, rock in zip(capacity, rocks)]
        remaining_capacity.sort()
        full_bags = 0

        for curr_capacity in remaining_capacity:
            if additionalRocks >= curr_capacity:
                additionalRocks -= curr_capacity
                full_bags += 1
            else:
                break

        return full_bags


def main():
    s = Solution()
    print(s.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 874 ms Beats 100%
   Memory 22.2 MB Beats 49.34%

2. Runtime 955 ms Beats 89.80% 
   Memory 22.1 MB Beats 69.41%
"""

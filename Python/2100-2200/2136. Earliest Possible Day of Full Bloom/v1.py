class Solution:
    def earliestFullBloom(self, plantTime: list[int],
                          growTime: list[int]) -> int:
        cur_plant_time = 0
        result = 0

        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x])

        for i in indices:
            cur_plant_time += plantTime[i]
            result = max(result, cur_plant_time + growTime[i])

        return result


def main():
    s = Solution()
    print(s.earliestFullBloom([1, 4, 3], [2, 3, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4831 ms, faster than 12.58% of Python3 online
submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 31.5 MB, less than 77.74% of Python3 online
submissions for Earliest Possible Day of Full Bloom.

2. Runtime: 4326 ms, faster than 30.64% of Python3 online
submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 31.6 MB, less than 70.32% of Python3 online
submissions for Earliest Possible Day of Full Bloom.
"""

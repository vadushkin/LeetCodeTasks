class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        data = list(zip(plantTime, growTime))
        data.sort(key=lambda x: -x[1])

        res = 0
        start_time = 0

        for plant, grow in data:
            start_time += plant
            res = max(res, start_time + grow)

        return res


def main():
    s = Solution()
    print(s.earliestFullBloom([1, 4, 3], [2, 3, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4030 ms, faster than 48.71% of Python3 online submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 34.8 MB, less than 36.77% of Python3 online submissions for Earliest Possible Day of Full Bloom.

2. Runtime: 3599 ms, faster than 59.68% of Python3 online submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 34.9 MB, less than 36.77% of Python3 online submissions for Earliest Possible Day of Full Bloom.
"""

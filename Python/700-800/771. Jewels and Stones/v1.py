class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        amount = 0
        for stone in jewels:
            amount += stones.count(stone)

        return amount


def main():
    s = Solution()
    print(s.numJewelsInStones("aA", "aAAb"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 38.22% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.8 MB, less than 59.78% of Python3 online submissions for Jewels and Stones.

2. Runtime: 38 ms, faster than 85.35% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 11.93% of Python3 online submissions for Jewels and Stones.
"""

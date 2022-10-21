class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))


def main():
    s = Solution()
    print(s.numJewelsInStones("aA", "aAAb"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 67.94% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 59.78% of Python3 online submissions for Jewels and Stones.

2. Runtime: 49 ms, faster than 67.94% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 11.93% of Python3 online submissions for Jewels and Stones.
"""

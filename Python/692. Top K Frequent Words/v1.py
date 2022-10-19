class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dictionary = {}
        for x in words:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1
        res = sorted(dictionary, key=lambda x: (-dictionary[x], x))
        return res[:k]


def main():
    s = Solution()
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 96.72% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 13.9 MB, less than 64.49% of Python3 online submissions for Top K Frequent Words.

2. Runtime: 130 ms, faster than 25.48% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 13.9 MB, less than 64.49% of Python3 online submissions for Top K Frequent Words.
"""

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        len_t, index = len(tokens) - 1, 0
        max_score, score = 0, 0

        while index <= len_t:
            if power >= tokens[index]:
                power -= tokens[index]
                index += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[len_t]
                len_t -= 1
                score -= 1
            else:
                break
        return max_score


def main():
    s = Solution()
    print(s.bagOfTokensScore([10000, 20, 3000, 2], 10))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 124 ms, faster than 8.49% of Python3 online submissions for Bag of Tokens.
Memory Usage: 13.9 MB, less than 77.36% of Python3 online submissions for Bag of Tokens.

2. Runtime: 103 ms, faster than 26.89% of Python3 online submissions for Bag of Tokens.
Memory Usage: 14 MB, less than 77.36% of Python3 online submissions for Bag of Tokens.
"""

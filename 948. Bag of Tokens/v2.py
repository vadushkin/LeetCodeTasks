class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        score, j, r = 0, 0, len(tokens) - 1
        tokens.sort()
        if len(tokens) == 0 or power < tokens[0]:
            return 0
        while j <= r:
            if power >= tokens[j]:
                score += 1
                power -= tokens[j]
                j += 1
            else:
                if r - j > 1:
                    power += tokens[r]
                    score -= 1
                    r -= 1
                else:
                    break
        return score


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 127 ms, faster than 7.08% of Python3 online submissions for Bag of Tokens.
Memory Usage: 14 MB, less than 39.62% of Python3 online submissions for Bag of Tokens.

2.  Runtime: 109 ms, faster than 19.81% of Python3 online submissions for Bag of Tokens.
Memory Usage: 14.1 MB, less than 39.62% of Python3 online submissions for Bag of Tokens.
"""

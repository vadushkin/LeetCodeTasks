class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        result = []
        ws = []
        for i, word in enumerate(words):
            ws.append((word, False, i, len(word)))
            ws.append((word[::-1], True, i, len(word)))
        ws.sort()

        for i, (a, a_reversed, a_idx, a_len) in enumerate(ws):
            for j in range(i + 1, len(ws)):
                b, b_reversed, b_idx, _ = ws[j]
                if b.startswith(a):
                    if a_idx != b_idx and a_reversed != b_reversed:
                        rest = b[a_len:]
                        if rest == rest[::-1]:
                            result.append([a_idx, b_idx] if b_reversed else [b_idx, a_idx])
                else:
                    break
        return result


def main():
    s = Solution()
    print(s.palindromePairs(["d", "gr", "dd", "rg"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 481 ms, faster than 99.69% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 27.5 MB, less than 41.37% of Python3 online submissions for Palindrome Pairs.

2. Runtime: 1190 ms, faster than 96.63% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 27.5 MB, less than 41.37% of Python3 online submissions for Palindrome Pairs.
"""

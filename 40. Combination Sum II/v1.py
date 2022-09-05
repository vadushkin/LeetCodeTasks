from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return
            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]
                if freq <= 0:
                    continue
                comb.append(candidate)
                counter[next_curr] = (candidate, freq - 1)
                backtrack(comb, remain - candidate, next_curr, counter, results)
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack(comb=[], remain=target, curr=0,
                  counter=counter, results=results)
        return results


def main():
    s = Solution()
    print(s.combinationSum2([1, 2, 2, 2, 5], 5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 81 ms, faster than 80.61% of Python3 online submissions for Combination Sum II.
Memory Usage: 14 MB, less than 23.45% of Python3 online submissions for Combination Sum II.

2. Runtime: 56 ms, faster than 94.91% of Python3 online submissions for Combination Sum II.
Memory Usage: 14 MB, less than 60.01% of Python3 online submissions for Combination Sum II.
"""

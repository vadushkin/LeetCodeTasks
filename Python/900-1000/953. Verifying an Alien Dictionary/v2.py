class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))



def main():
    s = Solution()
    print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 47 ms Beats 35.69%
   Memory 13.9 MB Beats 77.66%

2. Runtime 49 ms Beats 31.23%
   Memory 13.9 MB Beats 77.66%
"""

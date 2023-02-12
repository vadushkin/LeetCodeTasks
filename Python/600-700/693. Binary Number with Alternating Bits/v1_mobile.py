class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mid, bits = n >> 1, int(log2(n)) + 1

        p = n ^ (1 << bits) - 1

        return p == mid

class Solution:
    def binaryGap(self, N: int) -> int:
        return max(len(c) for c in bin(N)[2:].strip('0').split('1')) + 1 if N & (N-1) else 0

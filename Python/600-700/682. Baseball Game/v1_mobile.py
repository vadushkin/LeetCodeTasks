class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        [s.pop() if i == 'C' else s.append(2 * s[-1] if i == 'D' else s[-1] + s[-2] if i == '+' else int(i)) for i in operations]

        return sum(s)

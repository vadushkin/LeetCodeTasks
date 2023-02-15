class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [k for k, v in Counter(s1.split() + s2.split()).items() if v == 1]

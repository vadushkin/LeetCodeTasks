class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while "#" in S:S = re.sub("[a-z]?#", "", S,1)
        while "#" in T:T = re.sub("[a-z]?#", "", T,1)
        return S == T

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return set(map(''.join, product(*zip(S.lower(), S.upper()))))

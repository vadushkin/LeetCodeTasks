class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join([i.lower() for i in licensePlate if i.isalpha()])

        words = sorted(words, key=len)
        
        for word in words:
            for i in range(len(licensePlate)):
                if word.count(licensePlate[i]) < licensePlate.count(licensePlate[i]):
                    break
                if i == len(licensePlate)-1:
                    return word

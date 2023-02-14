class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        
        for i in range (left, right + 1):
            if all(i % x == 0 if x != 0 else False for x in map(int, str(i))):
                answer.append(i)
                
        return answer

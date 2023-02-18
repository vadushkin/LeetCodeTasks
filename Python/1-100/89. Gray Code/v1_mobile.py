class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:

            return [0]

        if n==1:

            return [0,1]

        if n==2:

            return [0,1,3,2]

        else:

            return self.grayCode(n - 1) + [x + (2 ** (n-1)) for x in self.grayCode(n - 1)[::-1]]

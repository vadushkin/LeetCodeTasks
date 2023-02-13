class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        return [ [i.start(),i.end() - 1] for i in re.finditer(r"{}".format("|".join( ["(?:{}){}".format(x,"{3,}")  for x in set(s)] )),s) ]

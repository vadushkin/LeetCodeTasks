class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        return [ele for x in zip(filter(lambda x: x%2==0, nums), filter(lambda x: x%2==1, nums)) for ele in x]

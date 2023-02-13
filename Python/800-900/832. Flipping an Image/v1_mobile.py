class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return map(partial(map, lambda x: 0 if x else 1), map(reversed, image))

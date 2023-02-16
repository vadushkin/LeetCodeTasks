class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        average, remainder, part, cnt = sum(arr) // 3, sum(arr) % 3, 0, 0

        for a in arr:

            part += a

            if part == average:

                cnt += 1

                part = 0

        return not remainder and cnt >= 3

class Solution:
    def trap(self, height: list[int]) -> int:
        ans = []
        start = {}
        _, b, ans = self.find_trapping_water(height, start, ans)
        if b:
            _, _, ans = self.find_trapping_water(height[-height[::-1].index(list(start.keys())[0]) - 1:][::-1], {},
                                                 ans)
        return sum(ans)

    @staticmethod
    def find_trapping_water(height, start, ans):
        for e, i in enumerate(height):
            if not start:
                start[i] = 0
                continue
            if list(start.values())[0] == 0 and i > list(start.keys())[0]:
                start.clear()
                start[i] = 0
                continue
            for key in start.keys():
                if key <= i and start[key] > 0:
                    ans.append(start[key])
                    start.pop(key)
                    if len(height) - 1 != e:
                        start[i] = 0
                    break
                else:
                    for key_w in start.keys():
                        start[key_w] += key_w - i
        return [height, start, ans]


def main():
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 487 ms, faster than 5.04% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16 MB, less than 44.51% of Python3 online submissions for Trapping Rain Water.

2. Runtime: 171 ms, faster than 72.96% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16.1 MB, less than 18.43% of Python3 online submissions for Trapping Rain Water.

3. Runtime: 323 ms, faster than 11.39% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16.1 MB, less than 18.43% of Python3 online submissions for Trapping Rain Water.
"""

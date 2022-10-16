class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not (0 <= c <= 2 ** 31 - 1):
            return False
        x, y = 0, 1
        list_sqrt_numbers = []
        while x <= c:
            list_sqrt_numbers.append(x)
            list_sqrt_numbers.append(x)
            x += y
            y += 2
        hash_map = {}
        for i, k in enumerate(list_sqrt_numbers):
            dif = c - k
            if dif in hash_map:
                return True
            hash_map[k] = i
        return False


s = Solution()
print(s.judgeSquareSum(4))


"""Tests:
1. Runtime: 773 ms, faster than 17.76% of Python3 online submissions for Sum of Square Numbers. O_O
Memory Usage: 22.6 MB, less than 7.20% of Python3 online submissions for Sum of Square Numbers. O_O

2. Runtime: 735 ms, faster than 18.90% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 22.4 MB, less than 7.20% of Python3 online submissions for Sum of Square Numbers.

3. Runtime: 720 ms, faster than 19.39% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 22.8 MB, less than 7.20% of Python3 online submissions for Sum of Square Numbers.
"""

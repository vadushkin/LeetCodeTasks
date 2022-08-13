from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if not (1 <= len(num)) <= 104 or not (1 <= k <= 10000):
            return []

        list_numbers = []
        for number in num:
            if not (0 <= number <= 9):
                return []
            # добавляем строки для join
            list_numbers.append(str(number))

        # str(int(''.join(list_numbers)) + k) == Из списка мы получаем строку: ['1', '2', '3'] - '123';
        # делаем число 123 и прибавляем k; возвращаем str(123 + k)
        return [int(number) for number in str(int(''.join(list_numbers)) + k)]


s = Solution()
print(s.addToArrayForm([1], 1))
"""Tests:
1. Runtime: 362 ms, faster than 75.92% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 51.67% of Python3 online submissions for Add to Array-Form of Integer.

2. Runtime: 423 ms, faster than 61.00% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 51.67% of Python3 online submissions for Add to Array-Form of Integer.
"""
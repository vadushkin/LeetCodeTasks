class Solution:
    def discountPrices(self, s: str, d: int) -> str:
        return ' '.join(
            (f"${(int(w[1:]) * (1 - (d / 100))):.2f}" if w.startswith('$') and w[1:].isnumeric() else w for w in
             s.split()))  # O______________________O


s = Solution()
print(s.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100))

"""Tests:
1. Runtime: 149 ms, faster than 85.64% of Python3 online submissions for Apply Discount to Prices.
Memory Usage: 16.9 MB, less than 15.12% of Python3 online submissions for Apply Discount to Prices.

2. Runtime: 183 ms, faster than 69.11% of Python3 online submissions for Apply Discount to Prices.
Memory Usage: 16.5 MB, less than 28.83% of Python3 online submissions for Apply Discount to Prices.

3. Runtime: 139 ms, faster than 89.85% of Python3 online submissions for Apply Discount to Prices.
Memory Usage: 17 MB, less than 9.83% of Python3 online submissions for Apply Discount to Prices.

4. Runtime: 141 ms, faster than 88.98% of Python3 online submissions for Apply Discount to Prices.
Memory Usage: 16.6 MB, less than 28.83% of Python3 online submissions for Apply Discount to Prices.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        for i in range(31):
            if 2 ** i == n:
                return True
        return False


def main():
    s = Solution()
    print(s.isPowerOfTwo(1024))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 82 ms, faster than 5.22% of Python3 online submissions for Power of Two.
Memory Usage: 13.8 MB, less than 95.76% of Python3 online submissions for Power of Two.

2. Runtime: 53 ms, faster than 47.44% of Python3 online submissions for Power of Two.
Memory Usage: 13.8 MB, less than 95.76% of Python3 online submissions for Power of Two.

3. Runtime: 66 ms, faster than 16.48% of Python3 online submissions for Power of Two.
Memory Usage: 13.7 MB, less than 95.76% of Python3 online submissions for Power of Two.

4. Runtime: 47 ms, faster than 63.05% of Python3 online submissions for Power of Two.
Memory Usage: 13.9 MB, less than 53.53% of Python3 online submissions for Power of Two.
"""

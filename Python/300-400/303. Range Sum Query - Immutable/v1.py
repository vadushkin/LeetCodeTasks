class NumArray:

    def __init__(self, nums: list[int]):
        self._nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self._nums[left:right + 1])


def main():
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print(n.sumRange(0, 2))
    print(n.sumRange(2, 5))
    print(n.sumRange(0, 5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2332 ms Beats 13.35%
   Memory 17.4 MB Beats 86.84%

2. Runtime 2332 ms Beats 13.35%
   Memory 17.4 MB Beats 86.84%
"""

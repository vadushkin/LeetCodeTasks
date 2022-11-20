class NumArray:

    def __init__(self, nums: list[int]):
        total = 0
        self.sum_list = [total := total + i for i in nums]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_list[right]

        return self.sum_list[right] - self.sum_list[left - 1]


def main():
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print(n.sumRange(0, 2))
    print(n.sumRange(2, 5))
    print(n.sumRange(0, 5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 77 ms Beats 97.69%
   Memory 17.8 MB Beats 34.79%
 
2. Runtime 183 ms Beats 55.29%
   Memory 17.9 MB Beats 10.32%
"""

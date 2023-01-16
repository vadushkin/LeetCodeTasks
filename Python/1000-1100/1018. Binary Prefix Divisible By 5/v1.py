class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        string = ''
        answer = []

        for i in range(len(nums)):
            string += str(nums[i])

            if not int(string, 2) % 5:
                answer.append(True)
            else:
                answer.append(False)

        return answer


def main():
    s = Solution()
    print(s.prefixesDivBy5([0, 1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1197 ms Beats 40.22%
   Memory 15.2 MB Beats 28.65%

2. Runtime 1271 ms Beats 32.78%
   Memory 15.1 MB Beats 52.62%
"""

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters)

        while left < right:
            mid = (left + right) // 2

            if ord(letters[mid]) == ord(target):
                if mid + 1 == len(letters):
                    return letters[0]

                if letters[mid + 1] == target:
                    for i in letters[mid:]:
                        if i != target:
                            return i
                    else:
                        return letters[0]
                return letters[mid + 1]

            elif ord(letters[mid]) > ord(target):
                right = mid
            else:
                left = mid + 1

        return letters[left] if left < len(letters) else letters[0]


def main():
    s = Solution()
    print(s.nextGreatestLetter(["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], "q"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 104 ms Beats 95.16% 
   Memory 14.3 MB Beats 74.68%

2. Runtime 109 ms Beats 83.40% 
   Memory 14.2 MB Beats 74.68%
"""

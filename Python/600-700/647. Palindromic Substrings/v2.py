class Solution:
    def countSubstrings(self, s: str) -> int:
        def algorithm_manachers(string):
            a = '@#' + '#'.join(string) + '#$'
            x = [0] * len(a)
            center = right = 0

            for i in range(1, len(a) - 1):
                if i < right:
                    x[i] = min(right - i, x[2 * center - i])

                while a[i + x[i] + 1] == a[i - x[i] - 1]:
                    x[i] += 1

                if i + x[i] > right:
                    center, right = i, i + x[i]

            return x

        return sum((v + 1) // 2 for v in algorithm_manachers(s))


def main():
    s = Solution()
    print(s.countSubstrings("aaav"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 48 ms Beats 99.17% 
   Memory 14 MB Beats 33.81%

2. Runtime 44 ms Beats 99.19% 
   Memory 13.8 MB Beats 67.44%
"""

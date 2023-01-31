class Solution:
    def closetTarget(self, words: list[str], target: str, start_index: int) -> int:
        n = len(words)

        for left in range(n):
            if words[(start_index + left) % n] == target:
                break
        else:
            return -1

        for right in range(n):
            if words[(start_index - right) % n] == target:
                break

        return min(left, right)


def main():
    s = Solution()
    print(s.closetTarget(
        ["pgmiltbptl", "jnkxwutznb", "bmeirwjars", "ugzyaufzzp", "pgmiltbptl", "sfhtxkmzwn", "pgmiltbptl", "pgmiltbptl",
         "onvmgvjhxa", "jyzdtwbwqp"], "pgmiltbptl", 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 41 ms Beats 99.51%
   Memory 14 MB Beats 52.15%

2. Runtime 48 ms Beats 91.62%
   Memory 14 MB Beats 52.15%
"""

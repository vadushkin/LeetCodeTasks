class Solution:
    def closetTarget(self, words: list[str], target: str, start_index: int) -> int:
        if words[start_index] == target:
            return 0

        answer = float("infinity")

        first_paces = 0
        second_paces = 0

        i = start_index + 1
        first_paces += 1

        while i != start_index:
            if i >= len(words):
                i = 0
                continue

            if words[i] == target:
                answer = min(answer, first_paces)
                break

            first_paces += 1
            i += 1

        j = start_index - 1
        second_paces += 1

        while j != start_index:
            if j < 0:
                j = len(words) - 1
                continue

            if words[j] == target:
                answer = min(answer, second_paces)
                break

            second_paces += 1
            j -= 1

        return answer if answer != float("infinity") else -1


def main():
    s = Solution()
    print(s.closetTarget(
        ["pgmiltbptl", "jnkxwutznb", "bmeirwjars", "ugzyaufzzp", "pgmiltbptl", "sfhtxkmzwn", "pgmiltbptl", "pgmiltbptl",
         "onvmgvjhxa", "jyzdtwbwqp"], "pgmiltbptl", 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 47 ms Beats 93.72%
   Memory 14 MB Beats 12.14%

2. Runtime 58 ms Beats 38.40%
   Memory 14.1 MB Beats 12.14%
"""

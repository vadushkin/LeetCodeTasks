class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def FindMinLen(ind, res_k, carry_over=0):

            if carry_over == 0 and dynamic[ind][res_k] != -1:
                return dynamic[ind][res_k]

            cur_count = carry_over + frequency[ind]

            min_len = 1 + min(len(str(cur_count)), cur_count - 1) + FindMinLen(ind + 1, res_k)

            for leave_count, code_count in [(0, 0), (1, 1), (9, 2), (99, 3)]:
                if cur_count > leave_count and res_k >= cur_count - leave_count:
                    min_len = min(min_len, code_count + FindMinLen(ind + 1, res_k - (cur_count - leave_count)))

            next_ind = chars.find(chars[ind], ind + 1)
            delete_count = sum(frequency[ind + 1:next_ind])
            if next_ind > 0 and res_k >= delete_count:
                min_len = min(min_len, FindMinLen(next_ind, res_k - delete_count, carry_over=cur_count))

            if carry_over == 0:
                dynamic[ind][res_k] = min_len
            return min_len

        frequency, chars = [], ""
        for char in s:
            if len(frequency) == 0 or char != chars[-1]:
                frequency.append(0)
                chars += char
            frequency[-1] += 1
        dynamic = [[-1] * (k + 1) for _ in range(len(frequency))] + [[0] * (k + 1)]

        return FindMinLen(0, k)


def main():
    s = Solution()
    print(s.getLengthOfOptimalCompression("abababababab", 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 856 ms, faster than 98.16% of Python3 online submissions for String Compression II.
Memory Usage: 14.6 MB, less than 85.89% of Python3 online submissions for String Compression II.

2. Runtime: 699 ms, faster than 99.39% of Python3 online submissions for String Compression II.
Memory Usage: 14.5 MB, less than 85.89% of Python3 online submissions for String Compression II.
"""

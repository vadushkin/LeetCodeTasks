class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []

        for i in range(1, len(s) - 2):
            seg_1 = s[:i]
            if not self.check_valid(seg_1):
                continue

            for j in range(i + 1, len(s) - 1):
                seg_2 = s[i:j]
                if not self.check_valid(seg_2):
                    continue

                for k in range(j + 1, len(s)):
                    seg_3 = s[j:k]
                    if not self.check_valid(seg_3):
                        continue

                    seg_4 = s[k:]
                    if not self.check_valid(seg_4):
                        continue

                    ans.append(seg_1 + '.' + seg_2 + '.' + seg_3 + '.' + seg_4)

        return ans

    @staticmethod
    def check_valid(seg):
        if seg.startswith('0') and seg != '0':
            return False

        if int(seg) > 255:
            return False

        return True


def main():
    s = Solution()
    print(s.check_valid("25525511135"))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 69 ms Beats 50.14%
   Memory 14 MB Beats 36.94%

2. Runtime 67 ms Beats 55.5%
   Memory 14 MB Beats 36.94%
"""

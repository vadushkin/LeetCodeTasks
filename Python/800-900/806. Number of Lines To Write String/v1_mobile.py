class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        a_dict = {l:w for l,w in zip("abcdefghijklmnopqrstuvwxyz",widths)}

        r_count, rp_count = 1, 0

        for i in range(len(s)):

            rp_count += a_dict[s[i]]

            if rp_count > 100:

                rp_count = a_dict[s[i]]

                r_count += 1

        return [r_count, rp_count]

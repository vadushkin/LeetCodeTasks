class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        hour_lst = [1, 2, 4, 8]
        min_lst = [1, 2, 4, 8, 16, 32]
        hour_pick_lst = []
        min_pick_lst = []
        rst = []

        def backtrack(count, pick_idx, hour_sum, min_sum):
            if count == turnedOn:
                hour_num = sum(hour_pick_lst)
                min_num = sum(min_pick_lst)
                min_str = "0" + str(min_num) if min_num < 10 else str(min_num)
                hour_str = str(hour_num)
                time = hour_str + ":" + min_str
                rst.append(time)
                return

            next_pick_idx = pick_idx + 1
            while 10 - next_pick_idx >= turnedOn - count:
                if next_pick_idx < len(hour_lst):
                    if hour_sum + hour_lst[next_pick_idx] < 12:
                        hour_pick_lst.append(hour_lst[next_pick_idx])
                        backtrack(count + 1, next_pick_idx, hour_sum + hour_lst[next_pick_idx], min_sum)
                        hour_pick_lst.pop(-1)
                    else:
                        next_pick_idx = len(hour_lst)
                        continue
                else:
                    if min_sum + min_lst[next_pick_idx - len(hour_lst)] < 60:
                        min_pick_lst.append(min_lst[next_pick_idx - len(hour_lst)])
                        backtrack(count + 1, next_pick_idx, hour_sum, min_sum + min_lst[next_pick_idx - len(hour_lst)])
                        min_pick_lst.pop(-1)
                    else:
                        break

                next_pick_idx += 1

        backtrack(0, -1, 0, 0)
        return rst


def main():
    s = Solution()
    print(s.readBinaryWatch(1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 72 ms, faster than 14.64% of Python3 online submissions for Binary Watch.
Memory Usage: 13.9 MB, less than 74.22% of Python3 online submissions for Binary Watch.

2. Runtime: 68 ms, faster than 21.28% of Python3 online submissions for Binary Watch.
Memory Usage: 14 MB, less than 30.79% of Python3 online submissions for Binary Watch.
"""

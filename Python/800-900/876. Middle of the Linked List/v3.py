from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]

        while arr[-1].next:
            arr.append(arr[-1].next)

        return arr[len(arr) // 2]


def main():
    s = Solution()
    print(s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 60 ms Beats 36.34%
   Memory 13.9 MB Beats 55.96%

2. Runtime 52 ms Beats 62.58%
   Memory 13.8 MB Beats 96.17%
"""

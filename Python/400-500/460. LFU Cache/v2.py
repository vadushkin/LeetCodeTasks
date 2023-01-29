from collections import OrderedDict
from collections import defaultdict


class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache(object):
    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2node[node.count][key]

        if not self.count2node[node.count]:
            del self.count2node[node.count]

        node.count += 1
        self.count2node[node.count][key] = node

        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)
            return

        if len(self.key2node) == self.cap:
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return


def main():
    pass


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 813 ms Beats 90.33%
   Memory 79.4 MB Beats 19.56%

2. Runtime 827 ms Beats 86.77%
   Memory 79.3 MB Beats 23.82%
"""

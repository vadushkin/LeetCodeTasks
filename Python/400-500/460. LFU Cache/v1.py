import collections


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel

        node.next.prev = node

        self._sentinel.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return

        if not node:
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev

        self._size -= 1

        return node


class LFUCache:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._node = dict()
        self._freq = collections.defaultdict(DLinkedList)
        self._min_freq = 0

    def _update(self, node):
        freq = node.freq

        self._freq[freq].pop(node)

        if self._min_freq == freq and not self._freq[freq]:
            self._min_freq += 1

        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key):
        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self._capacity == 0:
            return

        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._min_freq].pop()
                del self._node[node.key]
                self._size -= 1

            node = Node(key, value)

            self._node[key] = node
            self._freq[1].append(node)
            self._min_freq = 1
            self._size += 1


def main():
    pass


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 927 ms Beats 66.28% 
   Memory 78.2 MB Beats 62.95%

2. Runtime 903 ms Beats 71.69%
   Memory 78.1 MB Beats 62.95%
"""

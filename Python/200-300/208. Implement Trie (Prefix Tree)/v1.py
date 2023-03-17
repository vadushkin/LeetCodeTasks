class Trie:
    def __init__(self):
        self.hash_map = {}
        self.prefix_map = {}

    def insert(self, word: str) -> None:
        for index in range(len(word)):
            self.prefix_map[word[:index + 1]] = 1

        self.hash_map[word] = 1

    def search(self, word: str) -> bool:
        if self.hash_map.get(word, False):
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        if self.prefix_map.get(prefix, False):
            return True

        return False


def main():
    t = Trie()

    print(t.insert("a"))
    print(t.search("a"))
    print(t.startsWith("a"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 166 ms Beats 79.6% 
   Memory 25 MB Beats 96%

2. Runtime 156 ms Beats 85.87% 
   Memory 25.1 MB Beats 95.95%
"""

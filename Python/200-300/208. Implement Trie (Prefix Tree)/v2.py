class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}

            cur = cur[letter]

        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur:
                return False

            cur = cur[letter]

        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter not in cur:
                return False

            cur = cur[letter]

        return True


def main():
    t = Trie()

    print(t.insert("a"))
    print(t.search("a"))
    print(t.startsWith("a"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 133 ms Beats 91.14% 
   Memory 27.8 MB Beats 83.90%

2. Runtime 126 ms Beats 94.34% 
   Memory 27.4 MB Beats 92.85%
"""

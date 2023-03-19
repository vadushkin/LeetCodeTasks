class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root

        for char in word:
            node = node.setdefault(char, {})

        node[None] = None

    def search(self, word):
        def find(word_, node):
            if not word_:
                return None in node

            char, word_ = word_[0], word_[1:]

            if char != '.':
                return char in node and find(word_, node[char])

            return any(find(word_, kid) for kid in node.values() if kid)

        return find(word, self.root)


def main():
    wd = WordDictionary()

    print(wd.addWord("bad"))
    print(wd.addWord("dad"))
    print(wd.addWord("mad"))

    print(wd.search("pad"))
    print(wd.search("bad"))
    print(wd.search(".ad"))
    print(wd.search("b.."))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 7532 ms Beats 85.73% 
   Memory 55.5 MB Beats 95.57%

2. Runtime 7445 ms Beats 86.10% 
   Memory 55.5 MB Beats 95.32%
"""

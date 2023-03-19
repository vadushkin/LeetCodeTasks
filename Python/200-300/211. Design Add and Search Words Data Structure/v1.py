class WordDictionary:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        curr = self

        for symbol in word:
            if curr.children[ord(symbol) - ord('a')] is None:
                curr.children[ord(symbol) - ord('a')] = WordDictionary()
            curr = curr.children[ord(symbol) - ord('a')]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self

        for index in range(len(word)):
            symbol = word[index]

            if symbol == '.':
                for child in curr.children:
                    if child is not None and child.search(word[index + 1:]):
                        return True

                return False

            if curr.children[ord(symbol) - ord('a')] is None:
                return False

            curr = curr.children[ord(symbol) - ord('a')]

        return curr is not None and curr.isEndOfWord


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
1. Runtime 14737 ms Beats 8.97% 
   Memory 84 MB Beats 5.71% 

2. Runtime 14822 ms Beats 8.76% 
   Memory 83.4 MB Beats 7.45%
"""
